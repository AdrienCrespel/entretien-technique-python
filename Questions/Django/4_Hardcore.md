# Niveau Hardcore 🔴

## Comment implémentez-vous des API RESTful avec Django REST Framework (DRF) ?

**Réponse Attendue :**  
Django REST Framework (DRF) est une bibliothèque puissante pour créer des API RESTful avec Django. Vous pouvez définir des sérialiseurs, des vues et des routes pour gérer les requêtes API.  
**Exemple :**

```python
from rest_framework import serializers, viewsets
from .models import Personne

class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personne
        fields = '__all__'

class PersonneViewSet(viewsets.ModelViewSet):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
```

## Comment gérez-vous les transactions de base de données dans Django ?

**Réponse Attendue :**  
Django fournit un support pour les transactions de base de données à l'aide du décorateur `@transaction.atomic` ou du gestionnaire de contexte `transaction.atomic`. Cela permet de grouper plusieurs opérations de base de données dans une seule transaction.  
**Exemple :**

```python
from django.db import transaction

@transaction.atomic
def transfert_fonds(source, destination, montant):
    source.solde -= montant
    source.save()
    destination.solde += montant
    destination.save()
```

## Comment implémentez-vous des tâches asynchrones avec Celery dans Django ?

**Réponse Attendue :**  
Celery est une bibliothèque pour exécuter des tâches asynchrones dans Django. Vous pouvez définir des tâches en utilisant des fonctions décorées avec `@task` et les exécuter en arrière-plan.  
**Exemple :**

```python
from celery import shared_task

@shared_task
def envoyer_email(adresse_email):
    # Logique pour envoyer un email
    pass
```

## Comment implémentez-vous des websockets avec Django Channels ?

**Réponse Attendue :**  
Django Channels est une extension de Django pour gérer les websockets et les communications en temps réel. Vous pouvez définir des consommateurs pour gérer les connexions websocket.  
**Exemple :**

```python
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        await self.send(text_data=text_data)
```

## Comment implémentez-vous des tests d'intégration avec Django et Selenium ?

**Réponse Attendue :**  
Vous pouvez utiliser Selenium avec Django pour écrire des tests d'intégration qui simulent des interactions utilisateur dans un navigateur. Vous pouvez définir des tests en utilisant des classes de test et des méthodes de test.  
**Exemple :**

```python
from django.test import LiveServerTestCase
from selenium import webdriver

class MonTestDIntegration(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_titre_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Mon Titre', self.browser.title)
```