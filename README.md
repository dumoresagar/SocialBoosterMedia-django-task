# SocialBoosterMedia-django-task

# Django Demo: CRUD + 3rd-party integration + Visualization

## Summary
Small Django application that demonstrates:
- REST CRUD for `Item` model using Django REST Framework (DRF).
- Integration with a third-party API (JSONPlaceholder).
- A simple dashboard that visualizes DB data using Chart.js.
- for local development with Postgres.

## Features
- Endpoints:
  - `GET /api/items/` - list items
  - `POST /api/items/` - create item
  - `GET /api/items/<id>/` - retrieve
  - `PUT /api/items/<id>/` - update
  - `DELETE /api/items/<id>/` - delete
  - `GET /api/import-posts/` - fetch posts from JSONPlaceholder and save to DB
  - `GET /dashboard/` - Chart.js dashboard

## Quickstart (local with Docker)
1. Clone:
   ```bash
   git clone https://github.com/dumoresagar/SocialBoosterMedia-django-task.git

2. Create  Virtualenv
  1.python -m venv venv
  2. On Linux
    source venv/bin/activate
    On Windows
    venv\Scripts\activate 

3. cd demo_project

4.Run
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver

App will run at:
👉 http://127.0.0.1:8000/


Live Link : 