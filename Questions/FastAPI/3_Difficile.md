# Niveau Difficile 🟠

## Comment implémentez-vous l'authentification et l'autorisation dans FastAPI ?

**Réponse Attendue :**  
FastAPI permet d'implémenter l'authentification et l'autorisation en utilisant des dépendances et des schémas de sécurité. Vous pouvez définir des schémas comme OAuth2, JWT, etc.  
**Exemple :**

```python
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

## Comment gérez-vous les connexions WebSocket dans FastAPI ?

**Réponse Attendue :**  
FastAPI permet de gérer les connexions WebSocket en utilisant des décorateurs comme @app.websocket. Vous pouvez définir des points de terminaison WebSocket pour des communications en temps réel.  
**Exemple :**

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
```

## Comment implémentez-vous des tests unitaires dans FastAPI ?

**Réponse Attendue :**  
FastAPI permet d'écrire des tests unitaires en utilisant des bibliothèques comme pytest et httpx. Vous pouvez créer des tests pour vos points de terminaison en utilisant TestClient.  
**Exemple :**

```python
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/")
def read_main():
    return {"Hello": "World"}

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
```

## Comment gérez-vous les migrations de base de données dans FastAPI ?

**Réponse Attendue :**  
FastAPI ne fournit pas de système de migration intégré, mais vous pouvez utiliser des bibliothèques comme Alembic pour gérer les migrations de base de données. Vous pouvez configurer Alembic pour générer et appliquer des migrations.  
**Exemple :**

```python
from alembic import command
from alembic.config import Config

alembic_cfg = Config("alembic.ini")
command.upgrade(alembic_cfg, "head")
```

## Comment implémentez-vous des tâches périodiques dans FastAPI ?

**Réponse Attendue :**  
FastAPI ne fournit pas de gestionnaire de tâches périodiques intégré, mais vous pouvez utiliser des bibliothèques comme APScheduler pour planifier des tâches périodiques.  
**Exemple :**

```python
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def my_task():
    print("Task executed")

scheduler.add_job(my_task, "interval", minutes=1)
scheduler.start()
```