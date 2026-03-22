# 📝 Blog Website

A Django-based blog platform that allows users to browse published blog posts, read detailed articles, and interact through contact and report pages. The application follows a clean MVC (Model-View-Template) structure and leverages Django’s built-in admin for content management.

---

## 🚀 Features

- 📚 **Blog Listing** — View all published posts sorted by newest first  
- 📖 **Blog Detail** — Read individual posts via SEO-friendly slug URLs  
- 📝 **Draft & Publish System** — Manage posts with draft/published states  
- 📩 **Contact Page** — Dedicated page for user inquiries  
- 🚨 **Report Page** — Users can report issues/content  
- 🔐 **Admin Panel** — Full content management using Django Admin  
- 👤 **Authentication** — Uses Django’s built-in User model  

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** Django Templates (HTML, CSS)
- **Authentication:** Django Built-in User System

---

## 📂 Project Structure

```bash
BlogWebsite/
│
├── BlogWebsite/          # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── myApp/                # Main blog application
│   ├── models.py         # Post model
│   ├── views.py          # ListView & DetailView
│   ├── urls.py           # App routing
│   ├── admin.py          # Admin panel config
│   ├── templates/
│   │   ├── base.html
│   │   ├── blogs.html
│   │   ├── blog_detail.html
│   │   ├── contact_us.html
│   │   └── report.html
│   └── scripts_add_posts.py
│
├── db.sqlite3
└── manage.py
⚙️ Setup & Installation
1️⃣ Clone the repository
git clone https://github.com/Ammar-khan04/Blog-Website.git
cd Blog-Website/BlogWebsite
2️⃣ Create & activate virtual environment
python -m venv venv

Activate:

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate
3️⃣ Install dependencies
pip install django
4️⃣ Run migrations
python manage.py migrate
5️⃣ Create superuser (Admin access)
python manage.py createsuperuser
6️⃣ Run development server
python manage.py runserver
🌐 Access the application

Blog: http://127.0.0.1:8000

Admin Panel: http://127.0.0.1:8000/admin

🧠 Data Model
Post Model
Field	Type	Description
title	CharField	Post title (max 200 characters)
content	TextField	Main blog content
author	ForeignKey	Linked to Django User
slug	SlugField	SEO-friendly URL identifier
status	IntegerField	0 = Draft, 1 = Published
created_at	DateTimeField	Auto-set on creation
updated_at	DateTimeField	Auto-set on update
🔄 Application Flow

Admin creates blog posts via Django Admin

Posts marked as Published appear on homepage

Users can:

Browse all blogs

View individual posts

Access contact/report pages

Slug-based routing ensures clean URLs

🔒 Admin Panel

Django Admin provides:

Create/Edit/Delete blog posts

Manage users

Control post status (Draft/Published)

🚧 Future Improvements

Add user authentication for frontend (login/signup)

Comments & discussion system

Rich text editor (CKEditor/Markdown)

Image uploads for blog posts

Pagination for blog listing

Search & filtering functionality

REST API (Django REST Framework)

Deployment (Docker + Cloud)

📦 Deployment Ideas

Backend: Render / Railway / AWS EC2

Database: PostgreSQL

Static Files: AWS S3 / Cloudinary

👨‍💻 Author

Ammar Khan
GitHub: https://github.com/Ammar-khan04

⭐ Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

📄 License

This project currently does not include a license.
You may add an MIT License if you plan to make it publicly reusable.
