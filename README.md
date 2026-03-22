# Blog Website

A Django-based blog platform where users can read published blog posts, view individual articles, and access contact and report pages.

## Features

- **Blog Listing** — View all published posts sorted by newest first
- **Blog Detail** — Read individual posts via clean slug-based URLs
- **Draft/Published System** — Posts support draft and published states
- **Contact Page** — Dedicated contact us page
- **Report Page** — Report page for users
- **Admin Panel** — Django admin for managing posts and users

## Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** Django Templates (HTML)
- **Authentication:** Django built-in User model

## Project Structure

BlogWebsite/
├── BlogWebsite/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── myApp/                # Main blog application
│   ├── models.py         # Post model (title, content, author, slug, status)
│   ├── views.py          # ListView and DetailView for posts
│   ├── urls.py           # URL routing
│   ├── admin.py          # Admin configuration
│   ├── templates/
│   │   ├── base.html
│   │   ├── blogs.html
│   │   ├── blog_detail.html
│   │   ├── contact_us.html
│   │   └── report.html
│   └── scripts_add_posts.py
├── manage.py
└── db.sqlite3



## Setup

1. Clone the repository
   ```bash
   git clone https://github.com/Ammar-khan04/Blog-Website.git
   cd Blog-Website/BlogWebsite
Create a virtual environment and install dependencies


python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install django
Run migrations


python manage.py migrate
Create a superuser (to add blog posts via admin)


python manage.py createsuperuser
Run the server


python manage.py runserver
Visit http://127.0.0.1:8000 for the blog and http://127.0.0.1:8000/admin to manage posts

Post Model
Field	Type	Description
title	CharField	Post title (max 200 chars)
content	TextField	Post body
author	ForeignKey	Linked to Django User
slug	SlugField	URL-friendly identifier
status	IntegerField	0 = Draft, 1 = Published
created_at	DateTimeField	Auto-set on creation
updated_at	DateTimeField	Auto-set on update


---
