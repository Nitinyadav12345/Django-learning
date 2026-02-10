how to create the virtual env
> python -m venv env

how to activate the virtual env
> env\Scripts\activate

> deactivate 


how to check all the installed packages. 
> pip freeze 

> pip install django

> django-admin startproject django_rest_main .

> python manage.py runserver

> python manage.py startapp <<Name>>

how to create the default database tables 

> Python manage.py migrate 

how to create a superuser

> python manage.py createsuperuser 

http://127.0.0.1:8000/admin/login/?next=/admin/

how to create the migrations 
> python manage.py makemigrations

> python manage.py migrate

Class Based Views:- 
class-based views provide more structured and organized way to handle requests using object-oriented principles. 

get() -> get the students 
post() -> create a student
put() -> update a student 
delete() -> delete a student
