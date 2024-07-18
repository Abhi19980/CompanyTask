# Django Blog Application

This is a simple blog application built using Django and Django REST Framework, featuring basic CRUD functionalities for posts and comments, user authentication, pagination, and the ability to like posts.

## Features

- User registration and authentication
- Create, read, update, and delete posts
- Create and list comments under each post
- Pagination for post lists
- Like posts and count the number of likes
- Token-based authentication for API access

## Setup Instructions

### Prerequisites

- Python 3.10+
- pip (Python package installer)
- Virtualenv (recommended)

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Abhi19980/NewTaskComp2.git
cd django-blog-app


```

2. Create and activate a virtual environment:

python -m venv task
source Scripts/activate # On Windows, use `task\Scripts\activate.bat`

3. Install the dependencies:

pip install -r requirements.txt

4.Apply database migrations:
python manage.py makemigrations
python manage.py migrate

5. Run the development server:

python manage.py runserver

6. API Endpoints

   1. User Registration: POST /api/register/
   2. Token Authentication: POST /api-token-auth/
   3. Post List/Create: GET /api/posts/, POST /api/posts/
   4. Post Retrieve/Update/Delete: GET /api/posts/{id}/, PUT /api/posts/{id}/, DELETE /api/posts/{id}/
   5. Post Like: PATCH /api/posts/{id}/like/
   6. Comment List/Create: GET /api/posts/{post_id}/comments/, POST /api/posts/{post_id}/comments/

7. Pytest testing
   1. pytest blog_app/tests/test_models.py
   2. pytest blog_app/tests/test_views.py
