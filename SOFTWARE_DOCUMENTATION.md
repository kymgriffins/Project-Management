# Construction Project Management — Software Documentation

## Quick summary
A cloud-ready Construction Project Management SaaS providing REST APIs for managing projects, daily records, materials, tasks (todos), invoices, blueprint/renders/uploads, and role-based users with JWT authentication. Built with Django + Django REST Framework, uses Cloudinary for media, and is deployable to Heroku/Cloud platforms.

## Features
- Project CRUD with site metadata (coordinates, topology, permissions, phases)
- Daily records (work completed, planned, issues, spendings)
- Materials and Material usage tracking per day
- Todos/Tasks with assignment, budgets, and comments
- Invoice and InvoiceItem management
- Document uploads (blueprints, renders, MEP, structurals, etc.) via Cloudinary
- User management with Roles & Permissions
- JWT authentication (access + refresh tokens)

## Architecture
- Django 4.1.7 backend
- Django REST Framework (API endpoints in `projectmgt` app)
- Authentication handled by `authentication` app using `djangorestframework-simplejwt`
- Cloudinary for media storage
- Database: intended for PostgreSQL (psycopg2 dependency), compatible with sqlite for development

## Key modules and files
- `projectmgt/models.py` — data models (Project, DailyRecord, Material, Todo, Invoice, etc.)
- `projectmgt/serializers.py` — DRF serializers used by the API
- `projectmgt/views.py` — API views (function-based using `@api_view`)
- `projectmgt/urls.py` — API route definitions (base path expected to be `/api/`)
- `authentication/*` — user model (custom `User`), registration endpoint, JWT token endpoints
- `requirements.txt` — pinned dependencies

## Data model overview (short)
- Project: client info, site details, phase, budget, related documents (blueprints, renders), supervisor/architect/foreman (User FK)
- DailyRecord: project FK, date, work completed/planned, spendings, materials (MaterialUsage), document links
- Material: name, unit_cost, unit
- MaterialUsage: material FK, daily_record FK, quantity
- Todo: title, assigned_to (Users), due_date, project FK, budget fields, comments
- Invoice & InvoiceItem: invoice grouping, line items, materials support
- Media models: Blueprint, Renders, MEP, Structurals, QS, Architecturals, Legals (CloudinaryField)

## API Reference (endpoints)
Base path: `/api/`

Authentication:
- `POST /api/auth/register/` — register user (fields: username, email, password, roles)
- `POST /api/auth/token/` — obtain JWT tokens (email, password) -> {access, refresh}
- `POST /api/auth/token/refresh/` — refresh access token

Projects:
- `GET /api/projects/` — list projects
- `POST /api/projects/` — create a project
- `GET /api/project/{id}/` — get project details
- `PUT/PATCH /api/project/{id}/` — update project
- `DELETE /api/project/{id}/` — delete project
- `GET /api/projectsrecords/{id}/` — get daily records for project

Daily Records:
- `GET /api/dailyrecords/` — list
- `POST /api/dailyrecords/` — create
- `GET /api/dailyrecord/{id}/` — get
- `PUT/PATCH/DELETE /api/dailyrecord/{id}/` — manage

Materials & Usage:
- `GET /api/materials/`, `POST /api/materials/`
- `GET /api/material/{id}/`, `PUT/PATCH/DELETE /api/material/{id}/`
- `GET /api/material/used/`, `POST /api/material/used/` (MaterialUsage)
- `GET /api/material/used/{id}/`, `PUT/PATCH/DELETE /api/material/used/{id}/`

Todos:
- `GET /api/todos/`, `POST /api/todos/`
- `GET /api/todos/{id}/`, `PUT/PATCH/DELETE /api/todos/{id}/`

Invoices:
- `GET /api/invoices/`, `POST /api/invoices/`
- `GET /api/invoices/{id}/`, `PUT/PATCH/DELETE /api/invoices/{id}/`
- `GET /api/invoice-items/`, `POST /api/invoice-items/`

Documents / Media:
- `GET/POST /api/blueprint/` — upload blueprints (multipart/form-data)
- `GET/POST /api/record_pic/` — upload record pictures
- `GET/POST /api/building/` — create building entries
- `GET/POST /api/renders/` — create/render images
- Other media endpoints: `/api/mep/`, `/api/structurals/`, `/api/qs/`, `/api/architecturals/`, `/api/legals/` (all support GET/POST and individual resource CRUD endpoints)

## Authentication and headers
- After obtaining `access` token from `/api/auth/token/`, include header in API requests:
  `Authorization: Bearer <access_token>`
- Use refresh token to call `/api/auth/token/refresh/` when the access token expires

## Environment & setup
1. Create virtualenv and install requirements:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Environment variables (use `.env` with django-environ):
- `DATABASE_URL` (postgres or sqlite)
- `CLOUDINARY_URL` (for media uploads)
- `SECRET_KEY`
- `DEBUG` (True/False)

3. Run migrations and create superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. Run development server:

```powershell
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/` (assuming `urls.py` routes include `projectmgt.urls` under `/api/`).

## Tests
- There are tests under `projectmgt/tests.py` and `authentication/tests.py` — run them with:

```powershell
python manage.py test
```

## Deployment notes
- Requirements include `django-heroku` and `gunicorn` for Heroku deployment.
- Cloudinary storage plugin is configured (`dj3-cloudinary-storage`) for media.
- `Procfile` present in project root; configure `DATABASE_URL` and other secrets in hosting environment.
