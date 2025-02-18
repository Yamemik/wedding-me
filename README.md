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
    USER ||--|{ ALBUM : makes    
    USER {
        int id PK
        date created_at
        string email
        string password
        string surname                
        string name                
        string patr "O"
		
        bool is_admin
    }
    ALBUM ||--|{ GROUP : haves
    ALBUM {
        int id PK
        string title
        bool visible
		
        int user_id FK       
    }
	GROUP {
        int id PK
        string title
        bool visible
        int album_id FK       
	}
	ALBUM |o--|{ PHOTO : haves
	GROUP |o--|{ PHOTO : haves
    PHOTO {
        int id PK
        date created_at
        string name
        string path
        
        int group_id FK
        int album_id FK
    }	
    USER |o--|{ PAYMENT : pays_for    
	PAYMENT {
        int id PK
        date created_at
		string title
        int user_id FK       
	}
    USER  |o--|{ COMMENT : write
    PHOTO |o--|{ COMMENT : haves    
	COMMENT {
		int id
		date created_at
		string text
		
        int user_id FK       
        int photo_id FK       
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
[ERD](https://www.mermaidchart.com/app/projects/fd09ee93-1435-4b78-923e-98d85a854631/diagrams/69b97eb7-3f73-4452-89ae-ade46339f9f9/version/v0.1/edit)
