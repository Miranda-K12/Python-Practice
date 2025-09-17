#  Initialize a New Django Project

## Project Description
This is a minimal Django project setup containing one application (`myApp`) and an admin interface.  
The project demonstrates how to:
- Install Django
- Set up a new Django project
- Create a Django application
- Create a Django superuser for managing the admin interface

## Python Version
Python  3.13.7

## Virtual Environment
Create a virtual environment:

```bash
python -m venv venv

Activate the virtual environment:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

Install Dependencies

Install required packages using requirements.txt:

pip install -r requirements.txt

Run Migrations

Before running the server, apply migrations:

python manage.py migrate

Run the Project

Start the Django development server:

python manage.py runserver


Visit the project in your browser:

http://127.0.0.1:8000/

Superuser (Admin Panel)

Create a superuser to access the Django admin panel:

python manage.py createsuperuser


Admin panel URL:

http://127.0.0.1:8000/admin/
