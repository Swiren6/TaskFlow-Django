# 📚 RAPPORT DÉTAILLÉ DU PROJET TASKFLOW

## Système de Gestion de Tâches avec Django

---

# TABLE DES MATIÈRES

1. [Introduction](#1-introduction)
2. [Objectifs du Projet](#2-objectifs-du-projet)
3. [Technologies Utilisées](#3-technologies-utilisées)
4. [Installation et Configuration](#4-installation-et-configuration)
5. [Architecture du Projet](#5-architecture-du-projet)
6. [Modèles de Données](#6-modèles-de-données)
7. [Application Tasks](#7-application-tasks)
8. [Application Accounts](#8-application-accounts)
9. [Templates et Interface](#9-templates-et-interface)
10. [Flux de Navigation](#10-flux-de-navigation)
11. [Sécurité](#11-sécurité)
12. [Conclusion](#12-conclusion)

---

# 1. INTRODUCTION

## 1.1 Présentation

TaskFlow est une application web complète de gestion de tâches (To-Do List) développée avec le framework Django. Cette application permet à plusieurs utilisateurs de créer des comptes personnels et de gérer leurs tâches de manière indépendante et sécurisée.

## 1.2 Contexte

Dans un monde où la productivité et l'organisation sont essentielles, disposer d'un outil de gestion de tâches efficace est devenu indispensable. TaskFlow répond à ce besoin en offrant une interface moderne, intuitive et des fonctionnalités avancées.

## 1.3 Portée du Projet

Ce projet couvre :
- L'authentification des utilisateurs (inscription, connexion, déconnexion)
- La gestion complète des tâches (CRUD)
- Un système d'historique avec restauration
- Un tableau de bord avec statistiques
- Une interface utilisateur moderne et responsive

---

# 2. OBJECTIFS DU PROJET

## 2.1 Objectifs Fonctionnels

| Objectif | Description | Statut |
|----------|-------------|--------|
| Multi-utilisateurs | Chaque utilisateur a son propre espace | ✅ |
| Authentification | Inscription et connexion sécurisées | ✅ |
| Gestion des tâches | Créer, modifier, supprimer des tâches | ✅ |
| Priorités | Trois niveaux de priorité | ✅ |
| Dates d'échéance | Suivi des deadlines | ✅ |
| Historique | Conservation des tâches supprimées | ✅ |
| Restauration | Récupération des tâches supprimées | ✅ |
| Actions en masse | Opérations sur plusieurs tâches | ✅ |

## 2.2 Objectifs Techniques

- Utiliser l'architecture MVT de Django
- Implémenter une base de données relationnelle
- Créer une interface responsive
- Assurer la sécurité des données
- Suivre les bonnes pratiques de développement

---

# 3. TECHNOLOGIES UTILISÉES

## 3.1 Backend

### Django 5.x
Django est un framework web Python de haut niveau qui encourage le développement rapide et une conception propre et pragmatique.

**Pourquoi Django ?**
- Framework complet (batteries included)
- ORM puissant pour la base de données
- Système d'authentification intégré
- Protection CSRF automatique
- Administration automatique
- Grande communauté

### Python 3.x
Langage de programmation utilisé par Django.

### SQLite
Base de données légère intégrée, parfaite pour le développement et les petites applications.

## 3.2 Frontend

### HTML5
Structure sémantique des pages web.

### CSS3
- Variables CSS pour la cohérence
- Flexbox et Grid pour la mise en page
- Animations et transitions
- Design responsive

### JavaScript (Vanilla)
- Interactions utilisateur
- Actions en masse
- Menu mobile
- Messages auto-disparition

## 3.3 Ressources Externes

### Google Fonts
- **DM Sans** : Police principale pour le corps du texte
- **Space Grotesk** : Police pour les titres et logo

---

# 4. INSTALLATION ET CONFIGURATION

## 4.1 Commandes d'Installation

### Étape 1 : Installer Django
```bash
pip install django
```
**Explication** : Cette commande installe le framework Django via pip, le gestionnaire de paquets Python.

### Étape 2 : Créer le projet
```bash
django-admin startproject todo_app
```
**Explication** : `django-admin` est l'utilitaire en ligne de commande de Django. `startproject` crée un nouveau projet avec la structure de base.

### Étape 3 : Naviguer dans le projet
```bash
cd todo_app
```

### Étape 4 : Créer l'application Tasks
```bash
python manage.py startapp tasks
```
**Explication** : `startapp` crée une nouvelle application Django. Une application est un module qui gère une fonctionnalité spécifique.

### Étape 5 : Créer l'application Accounts
```bash
python manage.py startapp accounts
```

### Étape 6 : Créer les dossiers de templates
```bash
mkdir templates
mkdir templates/tasks
mkdir templates/accounts
```
**Explication** : Les templates sont les fichiers HTML qui définissent l'interface utilisateur.

### Étape 7 : Créer les dossiers statiques
```bash
mkdir static
mkdir static/css
mkdir static/js
```
**Explication** : Les fichiers statiques incluent CSS, JavaScript et images.

### Étape 8 : Créer les migrations
```bash
python manage.py makemigrations
```
**Explication** : Cette commande analyse les modèles et crée des fichiers de migration qui décrivent les changements à apporter à la base de données.

### Étape 9 : Appliquer les migrations
```bash
python manage.py migrate
```
**Explication** : Applique les migrations à la base de données, créant les tables nécessaires.

### Étape 10 : Lancer le serveur
```bash
python manage.py runserver
```
**Explication** : Démarre le serveur de développement Django sur `http://127.0.0.1:8000/`.

## 4.2 Configuration de settings.py

### Applications Installées
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',      # Notre application de tâches
    'accounts',   # Notre application de comptes
]
```
**Explication** : Cette liste définit toutes les applications actives dans le projet. Les 6 premières sont des applications Django par défaut, les 2 dernières sont nos applications personnalisées.

### Configuration des Templates
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]
```
**Explication** : `DIRS` indique à Django où chercher les templates. `BASE_DIR / 'templates'` pointe vers notre dossier templates à la racine.

### Configuration des Fichiers Statiques
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```
**Explication** : Définit l'URL pour accéder aux fichiers statiques et le dossier où ils sont stockés.

### Configuration de l'Authentification
```python
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'tasks:dashboard'
LOGOUT_REDIRECT_URL = 'accounts:login'
```
**Explication** :
- `LOGIN_URL` : Page vers laquelle rediriger les utilisateurs non connectés
- `LOGIN_REDIRECT_URL` : Page après connexion réussie
- `LOGOUT_REDIRECT_URL` : Page après déconnexion

---

# 5. ARCHITECTURE DU PROJET

## 5.1 Architecture MVT (Model-View-Template)

Django utilise l'architecture MVT, une variation du pattern MVC :
```
┌─────────────────────────────────────────────────────────────┐
│                        UTILISATEUR                          │
│                            │                                │
│                            ▼                                │
│                    ┌──────────────┐                         │
│                    │     URL      │                         │
│                    │   (urls.py)  │                         │
│                    └──────┬───────┘                         │
│                           │                                 │
│                           ▼                                 │
│                    ┌──────────────┐                         │
│                    │     VIEW     │                         │
│                    │  (views.py)  │                         │
│                    └──────┬───────┘                         │
│                           │                                 │
│              ┌────────────┼────────────┐                    │
│              ▼                         ▼                    │
│       ┌──────────────┐          ┌──────────────┐           │
│       │    MODEL     │          │   TEMPLATE   │           │
│       │ (models.py)  │          │   (.html)    │           │
│       └──────┬───────┘          └──────────────┘           │
│              │                                              │
│              ▼                                              │
│       ┌──────────────┐                                      │
│       │   DATABASE   │                                      │
│       │  (SQLite)    │                                      │
│       └──────────────┘                                      │
└─────────────────────────────────────────────────────────────┘
```

### Model (Modèle)
- Définit la structure des données
- Gère l'interaction avec la base de données
- Fichier : `models.py`

### View (Vue)
- Contient la logique métier
- Traite les requêtes HTTP
- Fichier : `views.py`

### Template
- Définit la présentation HTML
- Utilise le langage de template Django
- Fichiers : `*.html`

## 5.2 Structure des Fichiers
```
todo_app/
│
├── todo_app/                    # Configuration du projet
│   ├── __init__.py             # Indique que c'est un package Python
│   ├── settings.py             # Configuration globale
│   ├── urls.py                 # Routes principales
│   ├── asgi.py                 # Config serveur ASGI
│   └── wsgi.py                 # Config serveur WSGI
│
├── tasks/                       # Application de gestion des tâches
│   ├── __init__.py
│   ├── models.py               # Modèles Task et UserProfile
│   ├── views.py                # Vues pour les tâches
│   ├── forms.py                # Formulaires
│   ├── urls.py                 # Routes de l'app tasks
│   └── admin.py                # Configuration admin
│
├── accounts/                    # Application de gestion des comptes
│   ├── __init__.py
│   ├── views.py                # Vues d'authentification
│   ├── forms.py                # Formulaires utilisateur
│   └── urls.py                 # Routes de l'app accounts
│
├── templates/                   # Templates HTML
│   ├── base.html               # Template de base
│   ├── tasks/
│   │   ├── dashboard.html
│   │   ├── task_list.html
│   │   ├── completed_tasks.html
│   │   ├── task_history.html
│   │   └── task_form.html
│   └── accounts/
│       ├── login.html
│       ├── register.html
│       ├── profile.html
│       └── change_password.html
│
├── static/                      # Fichiers statiques
│   ├── css/
│   └── js/
│
├── manage.py                    # Utilitaire de gestion Django
└── db.sqlite3                   # Base de données SQLite
```

---

# 6. MODÈLES DE DONNÉES

## 6.1 Diagramme Entité-Relation
```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│    ┌──────────────┐         ┌──────────────┐               │
│    │     USER     │         │    TASK      │               │
│    │   (Django)   │────────<│              │               │
│    │              │   1:N   │              │               │
│    └──────┬───────┘         └──────────────┘               │
│           │                                                 │
│           │ 1:1                                             │
│           │                                                 │
│    ┌──────▼───────┐                                        │
│    │ USERPROFILE  │                                        │
│    │              │                                        │
│    └──────────────┘                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 6.2 Modèle Task (tasks/models.py)
```python
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
```

### Explication des Champs

| Champ | Type | Description |
|-------|------|-------------|
| `user` | ForeignKey | Lien vers l'utilisateur propriétaire. `on_delete=CASCADE` supprime les tâches si l'utilisateur est supprimé |
| `title` | CharField | Titre de la tâche (max 200 caractères) |
| `description` | TextField | Description optionnelle (peut être vide) |
| `status` | CharField | Statut actuel avec choix prédéfinis |
| `priority` | CharField | Niveau de priorité |
| `due_date` | DateField | Date d'échéance optionnelle |
| `previous_status` | CharField | Sauvegarde du statut avant suppression (pour restauration) |
| `created_at` | DateTimeField | Date de création (automatique) |
| `updated_at` | DateTimeField | Date de dernière modification (automatique) |
| `completed_at` | DateTimeField | Date de complétion |
| `deleted_at` | DateTimeField | Date de suppression |

### Méthodes du Modèle Task
```python
def mark_completed(self):
    """Marquer la tâche comme complétée"""
    self.previous_status = self.status
    self.status = 'completed'
    self.completed_at = timezone.now()
    self.save()
```
**Explication** : Cette méthode change le statut à 'completed', enregistre l'heure de complétion et sauvegarde l'ancien statut.
```python
def soft_delete(self):
    """Suppression douce - déplace vers l'historique"""
    self.previous_status = self.status
    self.status = 'deleted'
    self.deleted_at = timezone.now()
    self.save()
```
**Explication** : Au lieu de supprimer définitivement, on change le statut à 'deleted'. Cela permet la restauration ultérieure.
```python
def restore(self, restore_to='created'):
    """Restaurer une tâche depuis l'historique"""
    self.status = restore_to
    self.deleted_at = None
    if restore_to == 'created':
        self.completed_at = None
    elif restore_to == 'completed' and not self.completed_at:
        self.completed_at = timezone.now()
    self.save()
```
**Explication** : Restaure une tâche supprimée vers 'created' ou 'completed' selon le choix.

### Propriétés du Modèle
```python
@property
def is_overdue(self):
    """Vérifie si la tâche est en retard"""
    if self.due_date and self.status == 'created':
        return self.due_date < timezone.now().date()
    return False
```
**Explication** : `@property` permet d'accéder à cette méthode comme un attribut (`task.is_overdue`). Retourne True si la date d'échéance est passée.

## 6.3 Modèle UserProfile
```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    avatar_color = models.CharField(max_length=7, default='#6366f1')
```

**Explication** : Ce modèle étend le modèle User de Django avec des informations supplémentaires. `OneToOneField` crée une relation 1:1 avec User.

### Signal pour Création Automatique
```python
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
```
**Explication** : Ce signal écoute la création d'un User. Quand un utilisateur est créé, un UserProfile est automatiquement créé pour lui.

---

# 7. APPLICATION TASKS

## 7.1 Configuration des URLs (tasks/urls.py)
```python
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('active/', views.task_list, name='task_list'),
    path('completed/', views.completed_tasks, name='completed_tasks'),
    path('history/', views.task_history, name='task_history'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('<int:pk>/complete/', views.task_complete, name='task_complete'),
    path('<int:pk>/uncomplete/', views.task_uncomplete, name='task_uncomplete'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('<int:pk>/restore/', views.task_restore, name='task_restore'),
    path('<int:pk>/permanent-delete/', views.task_permanent_delete, name='task_permanent_delete'),
    path('bulk-action/', views.bulk_action, name='bulk_action'),
]
```

### Explication des Routes

| Route | Paramètre | Description |
|-------|-----------|-------------|
| `''` | - | Tableau de bord |
| `'active/'` | - | Liste des tâches actives |
| `'<int:pk>/edit/'` | pk (ID) | Édition d'une tâche spécifique |
| `'bulk-action/'` | - | Actions en masse |

**Note** : `app_name = 'tasks'` permet d'utiliser des noms d'URL préfixés comme `tasks:dashboard`.

## 7.2 Vues (tasks/views.py)

### Vue Dashboard
```python
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
```

### Analyse Ligne par Ligne

1. **`@login_required`** : Décorateur qui exige que l'utilisateur soit connecté
2. **`Task.objects.filter(user=request.user)`** : Récupère uniquement les tâches de l'utilisateur connecté
3. **`exclude(status='deleted')`** : Exclut les tâches supprimées du total
4. **`due_date__lt=timezone.now().date()`** : Filtre les tâches dont la date est inférieure (<) à aujourd'hui
5. **`order_by('-updated_at')[:5]`** : Trie par date de modification décroissante, limite à 5
6. **`render(request, template, context)`** : Retourne la page HTML avec les données

### Vue Création de Tâche
```python
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
```

### Explication du Flux
```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│    Requête GET                  Requête POST             │
│        │                            │                    │
│        ▼                            ▼                    │
│  ┌───────────┐               ┌───────────┐              │
│  │ Formulaire│               │ Formulaire│              │
│  │   vide    │               │ avec données│            │
│  └─────┬─────┘               └─────┬─────┘              │
│        │                           │                    │
│        ▼                           ▼                    │
│  ┌───────────┐               ┌───────────┐              │
│  │ Afficher  │               │ Valider   │              │
│  │   page    │               │ formulaire│              │
│  └───────────┘               └─────┬─────┘              │
│                                    │                    │
│                         ┌──────────┴──────────┐         │
│                         │                     │         │
│                    Valide?                Invalide      │
│                         │                     │         │
│                         ▼                     ▼         │
│                   ┌───────────┐         ┌───────────┐   │
│                   │ Sauvegarder│        │ Réafficher│   │
│                   │ + Redirect │        │ + erreurs │   │
│                   └───────────┘         └───────────┘   │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### Vue Actions en Masse
```python
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
    # ... autres actions
```

### Explication

- **`@require_POST`** : N'accepte que les requêtes POST (sécurité)
- **`getlist('task_ids')`** : Récupère plusieurs valeurs avec le même nom
- **`pk__in=task_ids`** : Filtre les tâches dont l'ID est dans la liste
- **`HTTP_REFERER`** : URL de la page précédente (pour redirection)

## 7.3 Formulaires (tasks/forms.py)
```python
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter task title...',
                'autofocus': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Add a description (optional)...',
                'rows': 4,
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select',
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
        }
```

### Explication

- **`ModelForm`** : Génère automatiquement un formulaire basé sur un modèle
- **`fields`** : Liste des champs à inclure
- **`widgets`** : Personnalise le rendu HTML de chaque champ
- **`attrs`** : Attributs HTML ajoutés au champ

---

# 8. APPLICATION ACCOUNTS

## 8.1 Configuration des URLs (accounts/urls.py)
```python
app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
]
```

## 8.2 Vues d'Authentification (accounts/views.py)

### Vue d'Inscription
```python
def register(request):
    if request.user.is_authenticated:
        return redirect('tasks:dashboard')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.get_or_create(user=user)
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('tasks:dashboard')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})
```

### Flux d'Inscription
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  1. Utilisateur accède à /accounts/register/            │
│                     │                                   │
│                     ▼                                   │
│  2. Est-il déjà connecté ?                              │
│           │                                             │
│     ┌─────┴─────┐                                       │
│     │           │                                       │
│    Oui         Non                                      │
│     │           │                                       │
│     ▼           ▼                                       │
│  Redirect   3. Afficher formulaire                      │
│  Dashboard      │                                       │
│                 ▼                                       │
│           4. Soumission POST                            │
│                 │                                       │
│                 ▼                                       │
│           5. Validation                                 │
│                 │                                       │
│           ┌─────┴─────┐                                 │
│           │           │                                 │
│        Valide     Invalide                              │
│           │           │                                 │
│           ▼           ▼                                 │
│     6. Créer User   Afficher                            │
│     7. Créer Profile erreurs                            │
│     8. Login auto                                       │
│     9. Redirect                                         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Vue de Connexion
```python
def user_login(request):
    if request.user.is_authenticated:
        return redirect('tasks:dashboard')
    
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect('tasks:dashboard')
    else:
        form = UserLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})
```

### Explication

- **`authenticate()`** : Vérifie les identifiants et retourne l'utilisateur ou None
- **`login()`** : Crée la session utilisateur
- **`request.GET.get('next')`** : Permet de rediriger vers la page demandée avant connexion

### Vue Profil
```python
@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('accounts:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)
    
    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
```

### Explication

- **`get_or_create()`** : Récupère le profil ou le crée s'il n'existe pas
- **`instance=request.user`** : Pré-remplit le formulaire avec les données existantes
- **Deux formulaires** : Un pour User (Django), un pour UserProfile (personnalisé)

## 8.3 Formulaires (accounts/forms.py)

### Formulaire d'Inscription
```python
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, ...)
    first_name = forms.CharField(max_length=30, required=True, ...)
    last_name = forms.CharField(max_length=30, required=True, ...)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email
```

### Explication

- **`UserCreationForm`** : Formulaire Django pour création d'utilisateur avec validation de mot de passe
- **`clean_email()`** : Méthode de validation personnalisée pour vérifier l'unicité de l'email

---

# 9. TEMPLATES ET INTERFACE

## 9.1 Template de Base (base.html)

Le template de base utilise l'héritage de templates Django :
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}TaskFlow{% endblock %}</title>
    <!-- CSS -->
</head>
<body>
    {% if user.is_authenticated %}
        <!-- Interface connectée avec sidebar -->
        {% block content %}{% endblock %}
    {% else %}
        <!-- Interface de connexion -->
        {% block auth_content %}{% endblock %}
    {% endif %}
</body>
</html>
```

### Système de Blocs
```
┌──────────────────────────────────────────────────────────┐
│  base.html                                               │
│  ┌────────────────────────────────────────────────────┐  │
│  │ {% block title %}{% endblock %}                    │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ {% block content %}{% endblock %}                  │  │
│  │                                                    │  │
│  │   Contenu par défaut ou vide                       │  │
│  │                                                    │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
            │
            │ {% extends 'base.html' %}
            ▼
┌──────────────────────────────────────────────────────────┐
│  dashboard.html                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ {% block title %}Dashboard{% endblock %}           │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ {% block content %}                                │  │
│  │   <h1>Dashboard</h1>                               │  │
│  │   <!-- Contenu spécifique -->                      │  │
│  │ {% endblock %}                                     │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

## 9.2 Tags de Template Django

### Variables
```html
{{ variable }}           <!-- Affiche la valeur -->
{{ user.username }}      <!-- Accède à un attribut -->
{{ task.title|upper }}   <!-- Applique un filtre -->
```

### Tags de Contrôle
```html
{% if condition %}
    <!-- Si vrai -->
{% else %}
    <!-- Si faux -->
{% endif %}

{% for task in tasks %}
    {{ task.title }}
{% empty %}
    Aucune tâche
{% endfor %}
```

### Tags d'URL
```html
{% url 'tasks:dashboard' %}              <!-- URL simple -->
{% url 'tasks:task_edit' task.pk %}      <!-- URL avec paramètre -->
```

### Tags de Formulaire
```html
{% csrf_token %}         <!-- Token de sécurité obligatoire -->
{{ form.title }}         <!-- Champ de formulaire -->
{{ form.title.errors }}  <!-- Erreurs du champ -->
```

## 9.3 Design CSS

### Variables CSS
```css
:root {
    --bg-primary: #0a0a0f;
    --bg-secondary: #12121a;
    --text-primary: #f5f5f7;
    --accent-primary: #818cf8;
    --success: #22c55e;
    --danger: #ef4444;
    /* ... */
}
```

**Avantages** :
- Cohérence visuelle
- Modification facile du thème
- Maintenance simplifiée

### Classes Utilitaires
```css
.btn { /* Bouton de base */ }
.btn-primary { /* Bouton principal */ }
.btn-danger { /* Bouton danger */ }
.card { /* Carte conteneur */ }
.form-input { /* Champ de saisie */ }
```

---

# 10. FLUX DE NAVIGATION

## 10.1 Flux Utilisateur Non Connecté
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│    Page d'accueil (/)                                   │
│          │                                              │
│          ▼                                              │
│    Redirection vers /accounts/login/                    │
│          │                                              │
│    ┌─────┴─────┐                                        │
│    │           │                                        │
│    ▼           ▼                                        │
│  Login    Register                                      │
│    │           │                                        │
│    └─────┬─────┘                                        │
│          │                                              │
│          ▼                                              │
│    Dashboard (/tasks/)                                  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## 10.2 Flux de Gestion des Tâches
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│                    DASHBOARD                            │
│                        │                                │
│         ┌──────────────┼──────────────┐                 │
│         │              │              │                 │
│         ▼              ▼              ▼                 │
│    ┌─────────┐   ┌─────────┐   ┌─────────┐             │
│    │ Active  │   │Completed│   │ History │             │
│    │  Tasks  │   │  Tasks  │   │         │             │
│    └────┬────┘   └────┬────┘   └────┬────┘             │
│         │             │             │                   │
│    ┌────┴────┐   ┌────┴────┐   ┌────┴────┐             │
│    │         │   │         │   │         │             │
│    ▼         ▼   ▼         ▼   ▼         ▼             │
│ Complete  Delete  Uncomplete  Delete  Restore  Perm.   │
│    │         │       │         │        │     Delete   │
│    │         │       │         │        │        │     │
│    ▼         ▼       ▼         ▼        ▼        ▼     │
│ Completed  History  Active   History  Active/  Supprimé│
│                                       Completed         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## 10.3 Cycle de Vie d'une Tâche
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│    CRÉATION                                             │
│        │                                                │
│        ▼                                                │
│    ┌─────────┐                                          │
│    │ CREATED │ ◄──────────────────────────────┐        │
│    │ (Active)│                                │        │
│    └────┬────┘                                │        │
│         │                                     │        │
│    mark_completed()                      restore()     │
│         │                                     │        │
│         ▼                                     │        │
│    ┌──────────┐                               │        │
│    │COMPLETED │                               │        │
│    │          │                               │        │
│    └────┬─────┘                               │        │
│         │                                     │        │
│    soft_delete()                              │        │
│         │                                     │        │
│         ▼                                     │        │
│    ┌─────────┐                                │        │
│    │ DELETED │ ───────────────────────────────┘        │
│    │(History)│                                         │
│    └────┬────┘                                         │
│         │                                              │
│    permanent_delete()                                  │
│         │                                              │
│         ▼                                              │
│    ╔═════════╗                                         │
│    ║ SUPPRIMÉ║                                         │
│    ║DÉFINITIF║                                         │
│    ╚═════════╝                                         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

# 11. SÉCURITÉ

## 11.1 Protection CSRF

Django inclut une protection contre les attaques CSRF (Cross-Site Request Forgery) :
```html
<form method="post">
    {% csrf_token %}
    <!-- champs du formulaire -->
</form>
```

**Fonctionnement** :
1. Django génère un token unique par session
2. Le token est inclus dans chaque formulaire
3. À la soumission, Django vérifie que le token correspond
4. Si différent, la requête est rejetée

## 11.2 Décorateur @login_required
```python
@login_required
def ma_vue(request):
    # Cette vue n'est accessible qu'aux utilisateurs connectés
```

**Comportement** :
- Utilisateur connecté → Accès à la vue
- Utilisateur non connecté → Redirection vers LOGIN_URL

## 11.3 Isolation des Données
```python
# Toujours filtrer par utilisateur
tasks = Task.objects.filter(user=request.user)

# Vérifier la propriété lors de l'accès
task = get_object_or_404(Task, pk=pk, user=request.user)
```

**Principe** : Un utilisateur ne peut jamais accéder aux tâches d'un autre utilisateur.

## 11.4 Hashage des Mots de Passe

Django utilise PBKDF2 par défaut pour hasher les mots de passe :
```python
# Le mot de passe n'est jamais stocké en clair
# Django gère automatiquement le hashage
user = form.save()  # Le mot de passe est hashé automatiquement
```

## 11.5 Décorateur @require_POST
```python
@require_POST
def task_delete(request, pk):
    # Cette vue n'accepte que les requêtes POST
```

**Avantage** : Empêche les actions destructives via des liens GET.

---

# 12. CONCLUSION

## 12.1 Résumé du Projet

TaskFlow est une application web complète qui démontre les capacités du framework Django :

| Aspect | Réalisation |
|--------|-------------|
| **Architecture** | MVT bien structurée avec séparation claire |
| **Base de données** | Modèles relationnels avec ORM Django |
| **Authentification** | Système complet avec profils utilisateur |
| **Interface** | Design moderne, responsive, thème sombre |
| **Sécurité** | CSRF, login required, isolation des données |
| **UX** | Messages flash, actions en masse, recherche |

## 12.2 Compétences Acquises

1. **Django Framework**
   - Configuration de projet
   - Création d'applications
   - Système de routing
   - ORM et migrations

2. **Développement Web**
   - Architecture MVT
   - Formulaires et validation
   - Sessions et authentification
   - Templates et héritage

3. **Frontend**
   - CSS moderne (variables, flexbox, grid)
   - JavaScript vanilla
   - Design responsive
   - UX/UI

## 12.3 Améliorations Possibles

| Amélioration | Description |
|--------------|-------------|
| API REST | Ajouter Django REST Framework |
| Notifications | Rappels par email pour les échéances |
| Catégories | Organiser les tâches par catégories |
| Partage | Partager des tâches entre utilisateurs |
| Export | Exporter les tâches en PDF/CSV |
| Tests | Ajouter des tests unitaires et d'intégration |
| Déploiement | Configurer pour production (PostgreSQL, Nginx) |

## 12.4 Ressources

- [Documentation Django](https://docs.djangoproject.com/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [MDN Web Docs](https://developer.mozilla.org/)

---

**Fin du Rapport**

*Projet réalisé avec Django - Système de Gestion de Tâches TaskFlow*