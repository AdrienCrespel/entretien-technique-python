# Niveau Difficile 🟠

## Comment implémentez-vous l'authentification et l'autorisation dans Django ?

**Réponse Attendue :**
Django fournit un système d'authentification intégré pour gérer les utilisateurs, les groupes et les permissions. Vous pouvez utiliser des vues et des formulaires d'authentification pour gérer les connexions, les déconnexions et les inscriptions.
**Exemple :**

```python
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def connexion_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
```

## Comment gérez-vous les fichiers statiques et les médias dans Django ?

**Réponse Attendue :**
Les fichiers statiques (CSS, JavaScript, images) sont gérés en configurant `STATIC_URL` et `STATICFILES_DIRS` dans `settings.py`. Les fichiers médias (uploads d'utilisateurs) sont gérés en configurant `MEDIA_URL` et `MEDIA_ROOT`.

## Comment implémentez-vous des tests unitaires dans Django ?

**Réponse Attendue :**
Django fournit un framework de tests intégré pour écrire des tests unitaires. Vous pouvez créer des tests en utilisant des classes de test et des méthodes de test.
**Exemple :**

```python
from django.test import TestCase
from .models import Personne

class PersonneTestCase(TestCase):
    def setUp(self):
        Personne.objects.create(nom="Dupont", age=30)

    def test_personne_nom(self):
        personne = Personne.objects.get(nom="Dupont")
        self.assertEqual(personne.nom, "Dupont")
```

## Comment gérez-vous les signaux dans Django ?

**Réponse Attendue :**
Les signaux dans Django permettent de connecter des fonctions à des événements spécifiques, comme la sauvegarde ou la suppression d'un modèle. Vous pouvez définir des signaux en utilisant le module `django.dispatch`.
**Exemple :**

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Personne

@receiver(post_save, sender=Personne)
def signal_post_save(sender, instance, **kwargs):
    print(f"{instance.nom} a été sauvegardé.")
```

## Comment implémentez-vous des vues basées sur des classes (CBV) dans Django ?

**Réponse Attendue :**
Les vues basées sur des classes (CBV) dans Django permettent de structurer les vues en utilisant des classes plutôt que des fonctions. Vous pouvez utiliser des classes de vue génériques pour des tâches courantes.
**Exemple :**

```python
from django.views.generic import ListView
from .models import Personne

class PersonneListView(ListView):
    model = Personne
    template_name = 'personne_list.html'
    context_object_name = 'personnes'
```