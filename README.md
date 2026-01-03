# 🎬 Movie Review API (Django REST Framework)

A Django REST Framework backend that allows users to discover movies via **TMDB**, authenticate using **JWT**, and create and view reviews for real movies.

---

## ✨ Features

- 🔐 JWT Authentication
  - User registration
  - Login with access & refresh tokens
  - Logout
- 🎥 Movie search powered by TMDB API
- 📝 Movie reviews linked by TMDB external movie ID
- 📖 Fetch all reviews for a specific movie

---

## 🧠 How It Works

1. Users register and log in using JWT authentication
2. Authenticated users search for movies via the TMDB API
3. Movies are identified using their TMDB `external_id`
4. Users create reviews using the movie’s external ID
5. Anyone can fetch all reviews associated with a movie

Movies are **not stored locally** unless a review has been made. TMDB acts as the source.

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- SimpleJWT
- TMDB API

---

## 🔐 Authentication

This project uses **JWT (JSON Web Tokens)** via `djangorestframework-simplejwt`.

Include the access token in authenticated requests:

Authorization: Bearer <access_token>

---

## 📌 API Endpoints

### 👤 User Authentication

| Method | Endpoint | Description |
|------|---------|------------|
| POST | `/login/` | Obtain access & refresh tokens |
| POST | `/token/refresh/` | Refresh access token |
| POST | `/register/` | Register a new user |
| POST | `/logout/` | Logout user |

---

### 🎬 Movies (TMDB)

| Method | Endpoint | Description |
|------|---------|------------|
| GET | `/movies/search/?q=<movie name>/` | Search movies using TMDB API |

---

### 📝 Reviews

| Method | Endpoint | Description |
|------|---------|------------|
| GET | `/movies/<external_id>/reviews/` | Get all reviews for a movie |
| POST | `/movies/<external_id>/reviews/` | Create a review for a movie |

`external_id` refers to the movie’s TMDB ID.

---

## 🧪 Example Flow

1. User logs in and receives a JWT
2. User searches for a movie
3. TMDB returns a movie with ID `27205`
4. User posts a review at:

POST /movies/27205/reviews/

5. Reviews can be fetched using the same endpoint

---
