# SocialBoosterMedia-django-task

# Django Demo: CRUD + 3rd-party integration + Visualization


## Summary
Small Django application that demonstrates:
- REST CRUD for `Item` model using Django REST Framework (DRF).
- Integration with a third-party API (JSONPlaceholder).
- A simple dashboard that visualizes DB data using Chart.js.
- for local development with Postgres.


Live Link : 

Admin Panel link : http://54.163.216.101:8000/admin/

👉Username : admin
👉Password : admin@123

## Features
- Endpoints:
  - `GET http://54.163.216.101:8000/api/items/` - list items
  - `POST http://54.163.216.101:8000/api/items/` - create item
  - `GET http://54.163.216.101:8000/api/items/<id>/` - retrieve
  - `PUT http://54.163.216.101:8000/api/items/<id>/` - update
  - `DELETE http://54.163.216.101:8000/api/items/<id>/` - delete
  - `GET http://54.163.216.101:8000/api/import-posts/` - fetch posts from JSONPlaceholder and save to DB
  - `GET http://54.163.216.101:8000/dashboard/` - Chart.js dashboard

## ThirtParty API and 

  - `GET http://54.163.216.101:8000/api/import-posts/` - fetch posts from JSONPlaceholder and save to DB


## local Features
- Endpoints:
  - `GET /api/items/` - list items
  - `POST /api/items/` - create item
  - `GET /api/items/<id>/` - retrieve
  - `PUT /api/items/<id>/` - update
  - `DELETE /api/items/<id>/` - delete
  - `GET /api/import-posts/` - fetch posts from JSONPlaceholder and save to DB
  - `GET /dashboard/` - Chart.js dashboard

## Quickstart (local)
1. Clone:
   ```bash
   git clone https://github.com/dumoresagar/SocialBoosterMedia-django-task.git

2. Create  Virtualenv
  python -m venv venv

3. Activate Virtualenv file

  -`source venv/bin/activate` - On Linux
  - `venv\Scripts\activate ` - On Windows
 

3. cd demo_project

4.Run
  -python manage.py makemigrations
  -python manage.py migrate
  -python manage.py runserver

App will run at locally:
👉 http://127.0.0.1:8000/



## API Documentation (Swagger & ReDoc)

# This project includes interactive API documentation powered by Swagger (drf-yasg).

# Available Endpoints

Swagger UI → http://54.163.216.101:8000/swagger/

(Interactive interface to test APIs)

ReDoc UI → http://54.163.216.101:8000/redoc/

(Clean, structured documentation view)

Raw OpenAPI Schema

JSON: http://54.163.216.101:8000/swagger.json

YAML: http://54.163.216.101:8000/swagger.yaml