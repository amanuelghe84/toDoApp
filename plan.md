 Todo App
 - what is the app? definition and description
 - who are the users? elaboration
 - what are the activities performed in the app? bc, ac, rc
    - business activities [bc]
    - audit activities [ac]
    - reporting activities
 - scope of the app?  

A Todo App is a simple task management application that helps managers or
admins to organize and to track their daily activities. It demonstrates key concepts
like CRUD (create, read, update and delete) operations, user authentication and
database management. They can create, edit and complete tasks while managing
personal or team projects. This App showcases essential development skills such 
as business, audit and reporting activities.

Actors:
 - USER
 - MANAGER
 - ADMIN
Activities:
- USER RELATED ACTIVITIES
   - CREATE USER
   - UPDATE USER
   - DELETE USER
-  PROJECT RELATED ACTIVITIES
   - CREATE PROJECT
   - UPDATE PROJECT
   - DELETE PROJECT
- TASK RELATED ACTIVITIES
   - CREATE TASK
   - UPDATE TASK
   - DELETE TASK
- COMMON [ENUM]
  - CREATE
  - UPDATE 
  - DELETE
  
ENTITIES:
 - TASK
 - PROJECT

MODEL:
 - USERS [WITH ROLES]
  - ID: [id]
  - FULL_NAME: [fullName]
  - EMAIL: [email]
  - PASSWORD: [password] 
  - ROLES: [role:ENUM]
    - USER
    - MANAGER
    - ADMIN
  - CREATED_AT: [createdAt:datetime]
  - UPDATED_AT: [updatedAt:datetime]
  - IS_ACTIVE: [isActive:boolean]
 - TASK
   - ID: [id]
   - PROJECT_ID: [projectId:foreignKey]
   - ASSIGNED_TO: [assigned:foreignKey] 
   - DESCRIPTION: [description]
   - STATUS: [status:ENUM]
     - ASSIGNED
     - PENDING
     - COMPLETE
   - CREATED_AT: [createdAt:datetime]
   - UPDATED_AT: [updatedAt:datetime]
   - IS_ACTIVE: [isActive:boolean]
 - PROJECT
   - ID: [id]
   - NAME: [name]
   - DESCRIPTION: [description]
   - OWNER_ID: [ownerId:foreignKey]
   - CREATED_AT: [createdAt:datetime]
   - UPDATED_AT: [updatedAt:datetime] 
   - IS_ACTIVE: [isActive:boolean]
 - AUDIT
  - ID: [id]
  - ACTOR: [actor:foreignKey]
  - ACTION: [action:general_activity]
  - DETAIL: [detail:sub_activity]
  - CREATED_AT: [createdAt:datetime]
  - UPDATED_AT: [updatedAt:datetime]

RELATIONS:
- PROJECTS [MANY-ONE] MANAGER 
- TASK [MANY-ONE] MANAGER
- TASK [MANY-ONE] PROJECTS
- TASK [MANY-ONE] USER

API GROUPS:
- USER [roles => user, manager, admin] [PROTECT] [/users]
   - CREATE [POST] [/users]
      - ADMIN 
   - UPDATE [PUT/PATCH] [/users/<id>]
      - ADMIN
      - OWN USER
   - DELETE [DELETE] [/users/<id>]
      - ADMIN
      - OWN USER
   - READ  [GET] [/users/<id>]
      - ADMIN
      - OWN USER

- PROJECT  [/project]
   - CREATE [POST] [/projects]
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]
   - UPDATE [PUT/PATCH] [/projects/<id>]
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]
   - DELETE [DELETE] [/projects<id>]
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]  
   - READ [GET] [/projects<id>]
      - ADMIN [ALL]
      - MANAGER  [ALL]
      - USER [ALL]

- TASK [/task]
   - CREATE [POST] [/tasks]
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]
   - UPDATE [PUT/PATCH] [/tasks<id>]
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]
   - DELETE [DELETE] [/tasks<id>]
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]  
   - READ [GET] [/tasks<id>]
      - ADMIN [ALL]
      - MANAGER  [ALL]
      - USER [ALL]
- AUDIT [/audit]
   - CREATE [POST] [/audits]
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]
   - UPDATE [PUT/PATCH] [/audits<id>]
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]
   - DELETE [DELETE] [/audits<id>]
      - ADMIN [ FOR ALL]
      - MANAGER  [ OWN PROJECTS]  
   - READ [GET] [/audits<id>]
      - ADMIN [ALL]
      - MANAGER  [ALL]
      - USER [ALL]
  
- BACKGROUND TASKS
  - Audit background tasks


- SCHEMAS [RESPONSE AND REQUEST]
  
  - USER [/user]
     - POST REQUEST [/user]: [ UserPostRequest ] 
       - username
       - email 
       - password
       - role
     - POST RESPONSE [/user]: [ UserPostResponse ] 
       -  message
       -  status
       -  success
     - GET REQUEST [/user/<id>]: [ UserGetRequest ]
       -  id
       -  username
       -  email
       -  password
       -  role
     - GET RESPONSE [/user]: [ UserGetResponse ]
       -  message
       -  status
       -  success
     - PUT REQUEST [/user/<id>]: [  UserUpdateRequest]
       -  id
       -  username
       -  email
       -  password
       -  role
     - PUT RESPONSE [/user]: [ UserUpdateResponse]
       -  message
       -  status
       -  success
     - DELETE REQUEST [/user/<id>]: [ UserDeleteRequest]
       -  id
       -  username
       -  email
       -  password
       -  role
  - TASK [/task]
     - POST REQUEST [/task]: [ TaskPostRequest ]
       -  task_name
       -  username
       -  email
       -  password
       -  role
     - POST RESPONSE [/task]: [ TaskPostResponse ]
       -  message
       -  status
       -  success 
     - GET REQUEST [/task/<task_id>]: [ TaskGetRequest]
       -  task_id
       -  user_id
       -  username
       -  email
       -  password
       -  role
     - GET RESPONSE [/task/<task_id>]: [ TaskGetResponse]
       -  message
       -  status
       -  success
     - PUT REQUEST [/task/<task_id>]: [ TaskUpdateRequest]
       -  task_id
       -  user_id
       -  username
       -  email
       -  password
       -  role
     - PUT RESPONSE [/task]: [ TaskUpdateResponse]
       -  message
       -  status
       -  success
     - DELETE REQUEST [/task/<task_id>]: [ TaskDeleteRequest]
       -  task_id
       -  user_id
       -  username
       -  email
       -  password
       -  role
  - PROJECT [/project]
     - POST REQUEST [/project]: [ ProjectPostRequest]
       -  project_name
       -  username
       -  email
       -  password
       -  role
     - POST RESPONSE [/project]: [ ProjectPostResponse]
       -  message
       -  status
       -  success
     - GET REQUEST [/project/<project_id>]: [ ProjectGetRequest]
       -  project_id
       -  user_id
       -  username
       -  email
       -  password
       -  role
     - GET RESPONSE [/project]: [ ProjectGetResponse]
       -  message
       -  status
       -  success
     - PUT REQUEST [/project/<project_id>]: [ ProjectUpdateRequest]
       -  project_id
       -  user_id
       -  username
       -  email
       -  password
       -  role
     - PUT RESPONSE [/project]: [ ProjectUpdateResponse]
       -  message
       -  status
       -  success
     - DELETE REQUEST [/project/<project_id>]: [ ProjectDeleteRequest]
       -  project_id
       -  user_id
       -  username
       -  email
       -  password
       -  role
     - DELETE RESPONSE [/project/<project_id>]
       -  message
       -  status
       -  success                            

- REPOSITORIES:
   - USERS [CLASS]
     -
     -  
   - PROJECTS [CLASS]
     -
     -  
   - TASKS [CLASS]
     -
     -  
   - AUDIT [CLASS]
     -
     -  

- SERVICES:
   - ORM SERVICE [super class]
     -  USER [sub class]
     -  projects [sub class]
     - etc ...
     -  

- DEPENDENCIES:
  - AUTHENTICATION
  - AUTHORIZATION

- TESTS:
  - INTEGRATION
  - UNIT TEST [ IN THE FEATURE] 
   ....coming soon..........

- Security
  - AUTHENTICATION
    - JWT [JSON WEB TOKEN]
  - AUTHORIZATION   
    - RBAC [ROLE BASED ACCESS CONTROL] 
  - CACHE
    - REDIS SESSION STORE

- ENVIRONMENT
  - APP VARIABLES 
   - # Application settings
      APP_NAME=Books Catalog API
      APP_VERSION=0.1.0
      APP_DESCRIPTION=A simple FastAPI application
      APP_DEBUG=True
      APP_HOST=127.0.0.1
      APP_PORT=8000
      APP_RELOAD=True
      APP_API_DOCS_URL=/docs
      APP_REDOC_URL=/redoc
      APP_SCALARA_URL=/scalar
      APP_OPENAPI_URL=/openapi.json

   - # Security settings
      SECURITY_SECRET_KEY=your_super_secret_key_here
      SECURITY_JWT_ALGORITHM=HS256
      SECURITY_ACCESS_TOKEN_EXPIRE_MINUTES=30

   - # database settings
      DATABASE_HOST=localhost
      DATABASE_PORT=27019
      DATABASE_NAME=mydb
      DATABASE_USER=root
      DATABASE_PASSWORD=example
      DATABASE_AUTH_SOURCE=admin

   - # logger settings
      LOG_LEVEL=debug
      LOG_FORMAT=text #json #csv
      LOG_FILE=/var/log/app.log
      LOG_RETENTION=7d
      LOG_ROTATION=1d
      LOG_HANDLERS=console,file
      LOG_DATE_FORMAT=%Y-%m-%d %H:%M:%S
      LOG_HANDLERS=console,file
      
   - # Redis settings
      REDIS_HOST=localhost
      REDIS_PORT=6379
      REDIS_PASSWORD=???
      REDIS_DB=0
      REDIS_USERNAME=???
      REDIS_SSL=False
      REDIS_SSL_CERT_REQS=none
      REDIS_SOCKET_CONNECT_TIMEOUT=5
      REDIS_SOCKET_TIMEOUT=5
      REDIS_CONNECTION_POOL_MAX_CONNECTIONS=50
      REDIS_DECODE_RESPONSES=True

  - PLATFORM [DOCKER]
  - ORCHESTRATION: DOCKER COMPOSE
  - CONTAINERS
      - Python [LINUX CONTAINER FOR APP RUNNING]
      - Mongodb [ DOCUMENT BASED DATABASE]
      - Redis [ON MEMORY DATABASE]

-  LIBRARIES:
```
   fastapi 
   uvicorn 
   bcrypt
   python-multipart
   pydantic
   pydantic-settings 
   requests
   motor 
   beanie 
   pyjwt
   python-jose[cryptography] 
   passlib[bcrypt] 
   pytest
   pre-commit
   ruff
   mypy
```

- SCAFFOLDING
```
todoApp
├─ .vscode/ 
│  ├─ extensions.json
│  ├─ launch.json  
│  └─ settings.json
├─ app/
│  │  ├─ __init__.py
│  ├─ core/
│  │  ├─ __init__.py
│  │  ├─ api.py   # routs            
│  │  ├─ config.py # configuration
│  │  ├─ logging.py 
│  │  └─ db.py
|  | 
│  ├─ models/
│  │  ├─ __init__.py
│  │  ├─ user.py
│  │  ├─ project.py
│  │  └─ task.py
|  |
│  ├─ schemas/
│  │  ├─ __init__.py
│  │  ├─ user.py
│  │  ├─ project.py
│  │  ├─ task.py
│  │  └─ task_history.py
│  │
│  ├─ repositories/
│  │  ├─ __init__.py
│  │  └─ user_repo.py
|  |
│  ├─ services/
│  │  ├─ __init__.py
│  │  ├─ user_service.py
|  │  ├─ task_service.py
|  |  └─ reporting_service.py
|  |
│  └─ dependencies/
│     ├─ __init__.py
│     └─ auth.py
│     └─ common.py
|  
├─ tests/
│  └─ test_users.py
├─ main.py
├─ __init__.py
├─ .env.example
├─ .pre-commit-config.yaml
├─ .mypy.ini
├─ .python-version
├─ ruff.toml
├─ uv.lock
├─ plan.md
├─ .gitignore
├─ pyproject.toml
├─ docker-compose.yml
├─ pytest.ini
└─ README.md
```