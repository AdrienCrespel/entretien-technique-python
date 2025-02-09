# Niveau Moyen 🟡

## Qu'est-ce que l'ORM de Django et comment l'utilisez-vous ?

**Réponse Attendue :**  
L'ORM (Object-Relational Mapping) de Django permet de mapper des objets Python à des tables de base de données. Vous définissez des modèles en Python, et Django génère les tables de base de données correspondantes.  
**Exemple :**

```python
from django.db import models

class Personne(models.Model):
    nom = models.CharField(max_length=100)
    age = models.IntegerField()
```

## Comment gérez-vous les migrations de base de données dans Django ?

**Réponse Attendue :**  
Les migrations de base de données dans Django sont gérées à l'aide des commandes `makemigrations` et `migrate`. `makemigrations` crée de nouvelles migrations basées sur les changements dans les modèles, et `migrate` applique ces migrations à la base de données.

## Qu'est-ce que le système de templates de Django et comment l'utilisez-vous ?

**Réponse Attendue :**  
Le système de templates de Django permet de séparer la logique de présentation de la logique métier. Les templates sont des fichiers HTML avec des balises Django pour insérer des données dynamiques.  
**Exemple :**

```html
<h1>{{ titre }}</h1>
<p>{{ contenu }}</p>
```

## Comment gérez-vous les formulaires dans Django ?

**Réponse Attendue :**  
Django fournit un framework de formulaires pour créer et valider des formulaires. Vous pouvez définir des formulaires en utilisant des classes Python et les utiliser dans vos vues et templates.  
**Exemple :**

```python
from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

## Qu'est-ce que le middleware dans Django et à quoi sert-il ?

**Réponse Attendue :**  
Le middleware dans Django est un composant qui traite les requêtes et les réponses globalement pour un projet. Il peut être utilisé pour des tâches telles que l'authentification, la gestion des sessions, etc.