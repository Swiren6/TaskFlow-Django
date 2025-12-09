
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.utils import timezone

from .models import Task
from .forms import TaskForm


@login_required
def dashboard(request):
    user_tasks = Task.objects.filter(user=request.user)
    
    stats = {
        'total': user_tasks.exclude(status='deleted').count(),
        'created': user_tasks.filter(status='created').count(),
        'completed': user_tasks.filter(status='completed').count(),
        'deleted': user_tasks.filter(status='deleted').count(),
        'overdue': user_tasks.filter(
            status='created',
            due_date__lt=timezone.now().date()
        ).count(),
    }
    
    recent_tasks = user_tasks.exclude(status='deleted').order_by('-updated_at')[:5]
    
    due_soon = user_tasks.filter(
        status='created',
        due_date__gte=timezone.now().date(),
        due_date__lte=timezone.now().date() + timezone.timedelta(days=3)
    ).order_by('due_date')[:5]
    
    context = {
        'stats': stats,
        'recent_tasks': recent_tasks,
        'due_soon': due_soon,
    }
    return render(request, 'tasks/dashboard.html', context)


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user, status='created').order_by('-created_at')
    
    priority = request.GET.get('priority')
    if priority:
        tasks = tasks.filter(priority=priority)
    
    due_filter = request.GET.get('due')
    if due_filter == 'overdue':
        tasks = tasks.filter(due_date__lt=timezone.now().date())
    elif due_filter == 'today':
        tasks = tasks.filter(due_date=timezone.now().date())
    elif due_filter == 'week':
        tasks = tasks.filter(
            due_date__gte=timezone.now().date(),
            due_date__lte=timezone.now().date() + timezone.timedelta(days=7)
        )
    
    search = request.GET.get('search')
    if search:
        tasks = tasks.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )
    
    context = {
        'tasks': tasks,
        'current_priority': priority,
        'current_due': due_filter,
        'search_query': search or '',
    }
    return render(request, 'tasks/task_list.html', context)


@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(user=request.user, status='completed').order_by('-completed_at')
    
    search = request.GET.get('search')
    if search:
        tasks = tasks.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )
    
    context = {
        'tasks': tasks,
        'search_query': search or '',
    }
    return render(request, 'tasks/completed_tasks.html', context)


@login_required
def task_history(request):
    tasks = Task.objects.filter(user=request.user, status='deleted').order_by('-deleted_at')
    
    search = request.GET.get('search')
    if search:
        tasks = tasks.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )
    
    context = {
        'tasks': tasks,
        'search_query': search or '',
    }
    return render(request, 'tasks/task_history.html', context)


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, f'Task "{task.title}" created successfully!')
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'title': 'Create New Task',
        'button_text': 'Create Task',
    })


@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, f'Task "{task.title}" updated successfully!')
            
            if task.status == 'completed':
                return redirect('tasks:completed_tasks')
            elif task.status == 'deleted':
                return redirect('tasks:task_history')
            return redirect('tasks:task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'task': task,
        'title': 'Edit Task',
        'button_text': 'Save Changes',
    })


@login_required
@require_POST
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.mark_completed()
    messages.success(request, f'Task "{task.title}" marked as completed!')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success'})
    
    return redirect('tasks:task_list')


@login_required
@require_POST
def task_uncomplete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.mark_created()
    messages.success(request, f'Task "{task.title}" moved back to active tasks!')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success'})
    
    return redirect('tasks:completed_tasks')


@login_required
@require_POST
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    previous_status = task.status
    task.soft_delete()
    messages.success(request, f'Task "{task.title}" moved to history.')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success'})
    
    if previous_status == 'completed':
        return redirect('tasks:completed_tasks')
    return redirect('tasks:task_list')


@login_required
@require_POST
def task_restore(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user, status='deleted')
    restore_to = request.POST.get('restore_to', 'created')
    
    if restore_to not in ['created', 'completed']:
        restore_to = 'created'
    
    task.restore(restore_to)
    
    status_name = 'Active Tasks' if restore_to == 'created' else 'Completed Tasks'
    messages.success(request, f'Task "{task.title}" restored to {status_name}!')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success'})
    
    return redirect('tasks:task_history')


@login_required
@require_POST
def task_permanent_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user, status='deleted')
    title = task.title
    task.permanent_delete()
    messages.success(request, f'Task "{title}" permanently deleted.')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success'})
    
    return redirect('tasks:task_history')


@login_required
@require_POST
def bulk_action(request):
    task_ids = request.POST.getlist('task_ids')
    action = request.POST.get('action')
    
    if not task_ids:
        messages.warning(request, 'No tasks selected.')
        return redirect(request.META.get('HTTP_REFERER', 'tasks:task_list'))
    
    tasks = Task.objects.filter(pk__in=task_ids, user=request.user)
    count = tasks.count()
    
    if action == 'complete':
        for task in tasks:
            task.mark_completed()
        messages.success(request, f'{count} task(s) marked as completed.')
        return redirect('tasks:task_list')
    
    elif action == 'delete':
        for task in tasks:
            task.soft_delete()
        messages.success(request, f'{count} task(s) moved to history.')
        return redirect(request.META.get('HTTP_REFERER', 'tasks:task_list'))
    
    elif action == 'restore_created':
        for task in tasks.filter(status='deleted'):
            task.restore('created')
        messages.success(request, f'{count} task(s) restored to Active Tasks.')
        return redirect('tasks:task_history')
    
    elif action == 'restore_completed':
        for task in tasks.filter(status='deleted'):
            task.restore('completed')
        messages.success(request, f'{count} task(s) restored to Completed Tasks.')
        return redirect('tasks:task_history')
    
    elif action == 'permanent_delete':
        tasks.filter(status='deleted').delete()
        messages.success(request, f'{count} task(s) permanently deleted.')
        return redirect('tasks:task_history')
    
    return redirect(request.META.get('HTTP_REFERER', 'tasks:task_list'))