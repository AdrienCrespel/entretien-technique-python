# Niveau Moyen 🟡

## Comment gérez-vous les dépendances dans FastAPI ?

**Réponse Attendue :**
FastAPI permet de définir des dépendances en utilisant des fonctions décorées avec `Depends`. Les dépendances peuvent être injectées dans les routes pour réutiliser du code et gérer des tâches communes.
Exemple :

```python
from fastapi import Depends

def common_parameters(q: str = None):
    return {"q": q}

@app.get("/items/")
def read_items(commons: dict = Depends(common_parameters)):
    return commons
```

## Comment gérez-vous les erreurs et les exceptions dans FastAPI ?

**Réponse Attendue :**
FastAPI permet de définir des gestionnaires d'exceptions personnalisés en utilisant des décorateurs comme `@app.exception_handler`. Vous pouvez également utiliser des exceptions HTTP intégrées comme `HTTPException`.
Exemple :

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if (item_id == 0):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}
```

## Comment gérez-vous les fichiers statiques dans FastAPI ?

**Réponse Attendue :**
Vous pouvez servir des fichiers statiques dans FastAPI en utilisant `StaticFiles` de `starlette.staticfiles`.
Exemple :

```python
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")
```

## Comment gérez-vous les sessions et les cookies dans FastAPI ?

**Réponse Attendue :**
FastAPI permet de gérer les sessions et les cookies en utilisant des dépendances et des en-têtes de réponse. Vous pouvez définir des cookies en utilisant `Response`.
Exemple :

```python
from fastapi import Cookie

@app.get("/items/")
def read_items(session_id: str = Cookie(None)):
    return {"session_id": session_id}
```

## Comment gérez-vous les tâches d'arrière-plan dans FastAPI ?

**Réponse Attendue :**
FastAPI permet de définir des tâches d'arrière-plan en utilisant `BackgroundTasks`. Vous pouvez ajouter des tâches à exécuter après la réponse HTTP.
Exemple :

```python
from fastapi import BackgroundTasks

def write_log(message: str):
    with open("log.txt", "a") as log_file:
        log_file.write(message)

@app.post("/send-notification/{email}")
def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"Notification sent to {email}")
    return {"message": "Notification sent"}
```