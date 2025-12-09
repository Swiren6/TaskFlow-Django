# TaskFlow - Système de Gestion de Tâches

![Django](https://img.shields.io/badge/Django-5.x-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Description

TaskFlow est un système complet de gestion de tâches (To-Do) développé avec Django. Il permet à plusieurs utilisateurs de créer un compte, se connecter et gérer leurs tâches de manière personnalisée et sécurisée.

## ✨ Fonctionnalités

### Gestion des Utilisateurs
- ✅ Inscription avec email, prénom, nom et mot de passe
- ✅ Connexion/Déconnexion sécurisée
- ✅ Profil utilisateur personnalisable
- ✅ Changement de mot de passe
- ✅ Avatar avec couleur personnalisable

### Gestion des Tâches
- ✅ Créer de nouvelles tâches
- ✅ Modifier les tâches existantes
- ✅ Marquer les tâches comme complétées
- ✅ Supprimer les tâches (suppression douce)
- ✅ Niveaux de priorité (Basse, Moyenne, Haute)
- ✅ Date d'échéance avec alertes

### Historique et Restauration
- ✅ Les tâches supprimées vont dans l'historique
- ✅ Restaurer les tâches vers "Actives" ou "Complétées"
- ✅ Suppression permanente depuis l'historique

### Actions en Masse
- ✅ Sélectionner plusieurs tâches
- ✅ Compléter en masse
- ✅ Supprimer en masse
- ✅ Restaurer en masse

### Tableau de Bord
- ✅ Statistiques des tâches
- ✅ Tâches récentes
- ✅ Tâches à échéance proche
- ✅ Compteur de tâches en retard

### Interface Utilisateur
- ✅ Design moderne et élégant (thème sombre)
- ✅ Interface responsive (mobile-friendly)
- ✅ Recherche et filtres
- ✅ Messages de notification

## 🛠️ Technologies Utilisées

| Technologie | Description |
|-------------|-------------|
| **Django 5.x** | Framework web Python |
| **SQLite** | Base de données |
| **HTML5** | Structure des pages |
| **CSS3** | Styles et animations |
| **JavaScript** | Interactivité |
| **Google Fonts** | Typographie (DM Sans, Space Grotesk) |

## 📁 Structure du Projet
```
todo_app/
├── todo_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── tasks/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── accounts/
│   ├── __init__.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── templates/
│   ├── base.html
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
├── static/
│   ├── css/
│   └── js/
├── manage.py
└── db.sqlite3
```

## 🚀 Installation et Démarrage

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner ou télécharger le projet**
```bash
   cd todo_app
```

2. **Installer Django**
```bash
   pip install django
```

3. **Appliquer les migrations**
```bash
   python manage.py makemigrations
   python manage.py migrate
```

4. **Lancer le serveur**
```bash
   python manage.py runserver
```

5. **Accéder à l'application**
```
   http://127.0.0.1:8000/
```

## 📖 Guide d'Utilisation

### Créer un Compte
1. Accédez à la page d'accueil
2. Cliquez sur "Create one"
3. Remplissez le formulaire d'inscription
4. Cliquez sur "Create Account"

### Créer une Tâche
1. Connectez-vous à votre compte
2. Cliquez sur "New Task" dans la barre latérale
3. Remplissez le titre, description, priorité et date d'échéance
4. Cliquez sur "Create Task"

### Gérer les Tâches
- **Compléter** : Cliquez sur le cercle à gauche de la tâche
- **Modifier** : Cliquez sur l'icône crayon
- **Supprimer** : Cliquez sur l'icône poubelle

### Restaurer une Tâche
1. Allez dans "History"
2. Cliquez sur "Restore" pour restaurer la tâche
3. Ou "Delete" pour supprimer définitivement

## 🗄️ Modèles de Données

### Task (Tâche)
| Champ | Type | Description |
|-------|------|-------------|
| id | AutoField | Identifiant unique |
| user | ForeignKey | Utilisateur propriétaire |
| title | CharField | Titre de la tâche |
| description | TextField | Description détaillée |
| status | CharField | Statut (created/completed/deleted) |
| priority | CharField | Priorité (low/medium/high) |
| due_date | DateField | Date d'échéance |
| created_at | DateTimeField | Date de création |
| updated_at | DateTimeField | Date de modification |
| completed_at | DateTimeField | Date de complétion |
| deleted_at | DateTimeField | Date de suppression |

### UserProfile (Profil Utilisateur)
| Champ | Type | Description |
|-------|------|-------------|
| id | AutoField | Identifiant unique |
| user | OneToOneField | Utilisateur lié |
| bio | TextField | Biographie |
| phone | CharField | Numéro de téléphone |
| avatar_color | CharField | Couleur de l'avatar |

## 🔗 Routes de l'Application

### Tâches
| URL | Nom | Description |
|-----|-----|-------------|
| `/tasks/` | dashboard | Tableau de bord |
| `/tasks/active/` | task_list | Liste des tâches actives |
| `/tasks/completed/` | completed_tasks | Tâches complétées |
| `/tasks/history/` | task_history | Historique |
| `/tasks/create/` | task_create | Créer une tâche |
| `/tasks/<id>/edit/` | task_edit | Modifier une tâche |
| `/tasks/<id>/complete/` | task_complete | Marquer complète |
| `/tasks/<id>/delete/` | task_delete | Supprimer |
| `/tasks/<id>/restore/` | task_restore | Restaurer |

### Comptes
| URL | Nom | Description |
|-----|-----|-------------|
| `/accounts/register/` | register | Inscription |
| `/accounts/login/` | login | Connexion |
| `/accounts/logout/` | logout | Déconnexion |
| `/accounts/profile/` | profile | Profil |
| `/accounts/change-password/` | change_password | Changer mot de passe |

## 🔒 Sécurité

- Protection CSRF sur tous les formulaires
- Authentification requise pour accéder aux tâches
- Hashage des mots de passe avec Django
- Isolation des données par utilisateur
- Sessions sécurisées

## 🎨 Captures d'Écran

### Page de Connexion
Interface épurée avec formulaire de connexion centré.

### Tableau de Bord
Affiche les statistiques, tâches récentes et tâches à venir.

### Liste des Tâches
Vue complète avec filtres, recherche et actions rapides.

### Profil Utilisateur
Modification des informations personnelles et avatar.

## 👨‍💻 Auteur

Développé avec ❤️ en utilisant Django

## 📄 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, le modifier et le distribuer.

---

**TaskFlow** - Gérez vos tâches efficacement! 