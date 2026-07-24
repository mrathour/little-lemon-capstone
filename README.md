# Little Lemon Restaurant API

Backend capstone project for the Meta Back-End Developer Professional Certificate. A Django + Django REST Framework application for the Little Lemon restaurant, exposing an API for browsing the menu and managing table bookings, with token-based authentication via Djoser.

## Tech Stack

- Python 3.14
- Django 6.0
- Django REST Framework
- Djoser (authentication endpoints + token auth)
- MySQL

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mrathour/little-lemon-capstone.git
cd little-lemon-capstone
```

### 2. Install dependencies

This project uses [pipenv](https://pipenv.pypa.io/) to manage the virtual environment and dependencies (see `Pipfile`).

```bash
pip install pipenv
pipenv install
pipenv shell
```

### 3. Configure the database

The project is configured to use MySQL (see `littlelemon/settings.py`). Create a database and user matching the settings, or update `DATABASES` in `littlelemon/settings.py` with your own credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'restaurant',
        'USER': 'djangoadmin',
        'PASSWORD': 'employee123!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

> Note: credentials are currently hardcoded in `settings.py` for local development. For any real deployment, move `SECRET_KEY` and database credentials to environment variables and set `DEBUG = False`.

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (for Django admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

The site will be available at `http://127.0.0.1:8000/`.

## API Endpoints

Base URL: `http://127.0.0.1:8000/`

### Site

| Method | Endpoint | Description |
|---|---|---|
| GET | `/restaurant/` | Renders the restaurant landing page |
| GET | `/admin/` | Django admin site |

### Authentication (Djoser)

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/users/` | Register a new user |
| GET/PUT/PATCH/DELETE | `/auth/users/me/` | Retrieve or update the current user |
| POST | `/auth/token/login/` | Obtain an auth token (login) |
| POST | `/auth/token/logout/` | Invalidate the current auth token (logout) |
| POST | `/restaurant/api-token-auth/` | Obtain an auth token via DRF's built-in token view |
| \* | `/api-auth/` | DRF browsable API login/logout views |

Include the token on subsequent requests as an `Authorization` header:

```
Authorization: Token <your-token>
```

### Menu

All endpoints below require authentication.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/restaurant/menu/` | List all menu items |
| POST | `/restaurant/menu/` | Create a menu item |
| GET | `/restaurant/menu/{id}/` | Retrieve a single menu item |
| PUT/PATCH | `/restaurant/menu/{id}/` | Update a menu item |
| DELETE | `/restaurant/menu/{id}/` | Delete a menu item |

Menu item fields: `Title` (string), `Price` (decimal), `Inventory` (integer).

### Bookings

All endpoints below require authentication.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/restaurant/booking/tables/` | List all bookings |
| POST | `/restaurant/booking/tables/` | Create a booking |
| GET | `/restaurant/booking/tables/{id}/` | Retrieve a single booking |
| PUT/PATCH | `/restaurant/booking/tables/{id}/` | Update a booking |
| DELETE | `/restaurant/booking/tables/{id}/` | Delete a booking |

Booking fields: `Name` (string), `No_of_guests` (integer), `BookingDate` (datetime).

## Running Tests

Tests live in the `tests/` directory and cover the `Menu` model and the menu API view.

```bash
python manage.py test tests
```

## Project Structure

```
littlelemon/        # Project settings, root URLconf, WSGI/ASGI entry points
restaurant/          # App: models, views, serializers, admin, URLs
  templates/         # HTML templates (landing page, static CSS)
  static/img/        # Restaurant images
  migrations/        # Database migrations
tests/               # Model and view tests
manage.py
```
