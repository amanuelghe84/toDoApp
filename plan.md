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