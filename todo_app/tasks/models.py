from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('completed', 'Completed'),
        ('deleted', 'Deleted'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(blank=True, null=True)
    previous_status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def mark_completed(self):
        self.previous_status = self.status
        self.status = 'completed'
        self.completed_at = timezone.now()
        self.save()
    
    def mark_created(self):
        self.previous_status = self.status
        self.status = 'created'
        self.completed_at = None
        self.save()
    
    def soft_delete(self):
        self.previous_status = self.status
        self.status = 'deleted'
        self.deleted_at = timezone.now()
        self.save()
    
    def restore(self, restore_to='created'):
        self.status = restore_to
        self.deleted_at = None
        if restore_to == 'created':
            self.completed_at = None
        elif restore_to == 'completed' and not self.completed_at:
            self.completed_at = timezone.now()
        self.save()
    
    def permanent_delete(self):
        self.delete()
    
    @property
    def is_overdue(self):
        if self.due_date and self.status == 'created':
            return self.due_date < timezone.now().date()
        return False
    
    @property
    def is_due_soon(self):
        if self.due_date and self.status == 'created':
            days_until_due = (self.due_date - timezone.now().date()).days
            return 0 <= days_until_due <= 3
        return False


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    avatar_color = models.CharField(max_length=7, default='#6366f1')
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
    @property
    def initials(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name[0]}{self.user.last_name[0]}".upper()
        return self.user.username[:2].upper()


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()