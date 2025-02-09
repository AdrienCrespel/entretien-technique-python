# Niveau Facile 🟢

## Qu'est-ce que FastAPI et pourquoi est-il utilisé ?

**Réponse Attendue :**  
FastAPI est un framework web moderne pour Python, basé sur les types standards de Python et les annotations de type. Il est utilisé pour créer des API rapides et efficaces avec une validation automatique des données et une génération automatique de documentation interactive.

## Comment installez-vous FastAPI ?

**Réponse Attendue :**  
Vous pouvez installer FastAPI en utilisant pip : `pip install fastapi`. Vous aurez également besoin d'un serveur ASGI comme Uvicorn : `pip install uvicorn`.

## Comment démarrez-vous une application FastAPI de base ?

**Réponse Attendue :**  
Vous pouvez démarrer une application FastAPI de base en créant un fichier Python avec une instance de FastAPI et en utilisant Uvicorn pour exécuter l'application.  
Exemple :

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Exécuter avec : uvicorn mon_app:app --reload
```

## Qu'est-ce que la validation des données dans FastAPI et comment l'utilisez-vous ?

**Réponse Attendue :**  
FastAPI utilise Pydantic pour la validation des données. Vous pouvez définir des modèles de données en utilisant des classes Pydantic et les utiliser dans vos routes pour valider les données d'entrée.  
Exemple :

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    description: str = None
```

## Comment définissez-vous une route dans FastAPI ?

**Réponse Attendue :**  
Vous définissez une route dans FastAPI en utilisant des décorateurs comme `@app.get`, `@app.post`, etc., sur des fonctions de vue.  
Exemple :

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```