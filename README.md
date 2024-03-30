# REST API with Django
# Overview

This project is a RESTful API developed using Django and Django REST Framework. It provides functionalities for user profile management, authentication, posting status updates, and viewing status update feeds.

# Features
User Profile Management: Create, update, and view user profiles.
Authentication: Secure user authentication using token-based authentication.
Status Updates: Post, update, and delete status updates.
Status Feed: View status update feeds from other users.
Technologies Used
Django
Django REST Framework
Python
Vagrant
VirtualBox
Atom (Text Editor)
ModHeaders (for HTTP header manipulation)
# Installation

Install dependencies: pip install -r requirements.txt
Run migrations: python manage.py migrate
Create a superuser: python manage.py createsuperuser
Start the development server: python manage.py runserver
API Endpoints
User Profile: /api/profile/
GET: Retrieve user profiles
POST: Create a new user profile
Authentication: /api/auth/
POST: Authenticate user and generate JWT token
Status Updates: /api/status/
GET: Retrieve status updates
POST: Create a new status update
Status Feed: /api/feed/
GET: Retrieve status update feed
Usage
Register a new user using /api/profile/ endp
