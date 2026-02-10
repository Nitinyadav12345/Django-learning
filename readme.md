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

what are the mixins 
mixins are reusable code classed in opps that provide specific functionalities 
In django REST framework , mixins are used to add common functionality to views. 

Create
read delete update 

five built in mixins in django frame work 
ListModelMixin  list()
CreateModelMixin  create()
RetriewModelMixin  retrieve()
UpdateModelMixin    update()
DestroyModelMixin   destroy()

How to use the mixins 
Inherit the mixins and generics.GenericAPIView in class based views.
class Employees(mixins , generics.GenericAPIView)

generic.GenericAPIView -> it is fondational class for all the views in django and provide the format for it. 

{
    get()
    post()
    update()
    delete()
}

