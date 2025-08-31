# Movie Review App (Backend)

A Django + Django REST Framework backend for a movie review application.  
Includes JWT authentication, user registration, movies, reviews, likes, favorites, and API documentation using drf-spectacular.

## Features

- Custom user model with email login
- User registration and profile endpoints
- CRUD operations for movies
- CRUD operations for reviews
- Like/unlike reviews
- Favorite/unfavorite movies
- JWT authentication (SimpleJWT)
- API documentation with Swagger and ReDoc

## Tech Stack

- Python 3.11+
- Django 4.x
- Django REST Framework
- drf-spectacular
- SQLite (can be switched to PostgreSQL)

## Installation

1. Clone the repo:
```bash
git clone https://github.com/yourusername/Movie-review.git
cd Movie-review

# Windows
python -m venv env
env\Scripts\activate

# Linux / Mac
python -m venv env
source env/bin/activate


pip install -r requirements.txt



python manage.py makemigrations
python manage.py migrate



python manage.py createsuperuser


python manage.py runserver




## API Endpoints

### Users
- `POST /api/users/register/` – Register a new user  
- `GET /api/users/profile/` – Get user profile (JWT required)  

### JWT
- `POST /api/token/` – Obtain access and refresh token  
- `POST /api/token/refresh/` – Refresh token  

### Movies
- `GET /api/movies/` – List all movies  
- `POST /api/movies/` – Add a new movie  
- `PUT /api/movies/<id>/` – Update movie  
- `DELETE /api/movies/<id>/` – Delete movie  
- `POST /api/movies/<id>/favorite/` – Favorite/Unfavorite movie  

### Reviews
- `GET /api/reviews/` – List all reviews  
- `POST /api/reviews/` – Add a review  
- `PUT /api/reviews/<id>/` – Update review  
- `DELETE /api/reviews/<id>/` – Delete review  
- `POST /api/reviews/<id>/like/` – Like/Unlike review  

### API Documentation
- Swagger UI: `/api/docs/`  
- ReDoc: `/api/redoc/`
