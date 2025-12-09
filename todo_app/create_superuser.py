import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_app.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@taskflow.com',
        password='Admin123!TaskFlow',  # CHANGEZ CE MOT DE PASSE !
        first_name='Admin',
        last_name='TaskFlow'
    )
    print("✅ Superuser créé avec succès!")
else:
    print("ℹ️ Le superuser existe déjà")
