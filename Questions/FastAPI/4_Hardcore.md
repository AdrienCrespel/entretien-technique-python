# Niveau Hardcore 🔴

## Comment implémentez-vous des API GraphQL avec FastAPI ?

**Réponse Attendue :**
Vous pouvez implémenter des API GraphQL dans FastAPI en utilisant des bibliothèques comme graphene ou strawberry. Vous pouvez définir des schémas GraphQL et les intégrer avec FastAPI.

**Exemple :**
```python
import strawberry
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")
```

## Comment implémentez-vous des microservices avec FastAPI ?

**Réponse Attendue :**
Vous pouvez implémenter des microservices avec FastAPI en utilisant des conteneurs Docker et des orchestrateurs comme Kubernetes. Vous pouvez définir des services indépendants et les déployer en utilisant des fichiers Dockerfile et des configurations Kubernetes.

**Exemple :**
```dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
```

## Comment implémentez-vous des tâches asynchrones avec Celery dans FastAPI ?

**Réponse Attendue :**
Vous pouvez implémenter des tâches asynchrones avec Celery dans FastAPI en utilisant des dépendances et des tâches Celery. Vous pouvez définir des tâches Celery et les exécuter en arrière-plan.

**Exemple :**
```python
from celery import Celery

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task
def my_task(arg):
    print(f"Task executed with arg: {arg}")

@app.post("/run-task/")
def run_task(arg: str):
    my_task.delay(arg)
    return {"message": "Task started"}
```

## Comment implémentez-vous des tests d'intégration avec FastAPI et Docker ?

**Réponse Attendue :**
Vous pouvez implémenter des tests d'intégration avec FastAPI et Docker en utilisant des conteneurs Docker pour exécuter vos tests. Vous pouvez utiliser des bibliothèques comme pytest et docker-compose pour configurer et exécuter vos tests.

**Exemple :**
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:80"
  tests:
    build: .
    command: pytest
    depends_on:
      - app
```

## Comment implémentez-vous des API RESTful sécurisées avec FastAPI et OAuth2 ?

**Réponse Attendue :**
Vous pouvez implémenter des API RESTful sécurisées avec FastAPI et OAuth2 en utilisant des bibliothèques comme fastapi-users ou authlib. Vous pouvez définir des schémas de sécurité OAuth2 et les intégrer avec FastAPI.

**Exemple :**
```python
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication

SECRET = "SECRET"

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

fastapi_users = FastAPIUsers(
    get_user_manager,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

app.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)
```