# Django REST Framework - Project Setup & Guide

---

## 🛠️ Virtual Environment Setup

### Create a Virtual Environment
```bash
python -m venv env
```

### Activate the Virtual Environment
```bash
# Windows
env\Scripts\activate

# Mac/Linux
source env/bin/activate
```

### Deactivate the Virtual Environment
```bash
deactivate
```

---

## 📦 Package Management

### Check All Installed Packages
```bash
pip freeze
```

### Install Django
```bash
pip install django
```

---

## 🚀 Project Setup

### Create a Django Project
```bash
django-admin startproject django_rest_main .
```

### Run the Development Server
```bash
python manage.py runserver
```

### Create a New App
```bash
python manage.py startapp <<AppName>>
```

---

## 🗄️ Database & Migrations

### Create Default Database Tables
```bash
python manage.py migrate
```

### Create Migrations (After Model Changes)
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 Admin Setup

### Create a Superuser
```bash
python manage.py createsuperuser
```

### Access Admin Panel
```
http://127.0.0.1:8000/admin/login/?next=/admin/
```

---

## 📖 Class-Based Views (CBVs)

Class-based views provide a more **structured and organized** way to handle requests using **object-oriented principles**.

| HTTP Method | Purpose            |
|-------------|--------------------|
| `get()`     | Get the records    |
| `post()`    | Create a record    |
| `put()`     | Update a record    |
| `delete()`  | Delete a record    |

---

## 🧩 Mixins

Mixins are **reusable code classes** in OOP that provide specific functionalities.
In Django REST Framework, mixins are used to add **common functionality** to views.

### Five Built-in Mixins in Django REST Framework

| Mixin                  | Method       | Operation |
|------------------------|--------------|-----------|
| `ListModelMixin`       | `list()`     | Read All  |
| `CreateModelMixin`     | `create()`   | Create    |
| `RetrieveModelMixin`   | `retrieve()` | Read One  |
| `UpdateModelMixin`     | `update()`   | Update    |
| `DestroyModelMixin`    | `destroy()`  | Delete    |

### How to Use Mixins

Inherit the **mixins** along with `generics.GenericAPIView` in your class-based views:

```python
from rest_framework import generics, mixins

class Employees(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

### What is `generics.GenericAPIView`?

`generics.GenericAPIView` is the **foundational class** for all views in Django REST Framework. It provides the base structure and core functionality such as:

- Queryset handling
- Serializer integration
- Pagination support
- Filtering support

It acts as the **backbone** on top of which mixins add their specific behaviors (`get()`, `post()`, `put()`, `delete()`).

---