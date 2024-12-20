# Wedding Me (backend)

![Static Badge](https://img.shields.io/badge/Yamemik-WeddingMe-template)
![GitHub top language](https://img.shields.io/github/languages/top/Yamemik/wedding-me)
![GitHub](https://img.shields.io/github/license/Yamemik/wedding-me)
![GitHub Repo stars](https://img.shields.io/github/stars/Yamemik/wedding-me)
![GitHub issues](https://img.shields.io/github/issues/Yamemik/wedding-me)


## Общее описание
_____

### Стек технологий:
  - FastAPI;
  - postgreSQL;
  - docker;
  - docker-compose.


## Техническое описание
_____

### ER-Diagrams
```mermaid
erDiagram
    USER ||--|{ GALLERY : makes    
    USER {
        int id PK
        date created_at
        string email "*"
        string password "*"
        string surname                
        string name                
        string patr                
        bool is_admin "*"
    }
    GALLERY ||--|{ GROUP : haves
    GALLERY {
        int id PK
        string title
        int user_id FK       
    }
    GROUP ||--|{ PHOTO : haves   
    GROUP {
        int id PK
        string title "*"
        
        int gallery_id FK "*"
    }
    PHOTO {
        int id PK
        date created_at
        string name "*"
        string path "*"
        
        int group_id FK "*"
    }
```

### fastapi
```bash
# запустить сервер
$ uvicorn --factory src.main:create_app --reload
```

### команды MakeFile
```bash
# запустить контейнер с приложением
$ make app
# запустить контейнер с приложением
$ make storage
```

### docker & docker-compose
```bash
# собрать
$ docker compose -f docker_compose/app.yaml up
# ребилдинг
$ docker build --no-cache -t docker_compose-fastapi .
```

### PipENV
```bash
# install pipenv
pip install pipenv
# .venv in fold of the project
$env:PIPENV_VENV_IN_PROJECT=1
# initilization
pipenv shell
# install
pipenv install
```


## Ссылки
_____
[by Yamemik](https://github.com/Yamemik)
[ТЗ](https://docs.google.com/document/d/1KUIepvxzV8rNgzTm7u0jYfLznHQ3HfmMgL96vpWOmVI/edit?usp=sharing)
