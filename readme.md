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
## 📖 Generics in Django REST Framework

Generics are **pre-built class-based views** provided by Django REST Framework that combine `GenericAPIView` with **mixins** automatically, so you don't have to write repetitive code.

Instead of manually inheriting mixins and writing `get()`, `post()`, `put()`, `delete()` methods, generics **handle everything for you** out of the box.

---

### 🔄 Comparison: Mixins vs Generics

**With Mixins (More Code):**
```python
from rest_framework import generics, mixins

class EmployeeList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

**With Generics (Less Code - Same Result):**
```python
from rest_framework import generics

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
```

> ✅ Both do the **exact same thing**, but generics save you from writing boilerplate code.

---

### 📋 Basic Generic Views (Single Operation)

| Generic View        | Operation                              | HTTP Method |
|---------------------|----------------------------------------|-------------|
| `ListAPIView`       | List all objects                       | `GET`       |
| `CreateAPIView`     | Create a new object                    | `POST`      |
| `RetrieveAPIView`   | Retrieve a single object using `pk`    | `GET`       |
| `UpdateAPIView`     | Update a single object using `pk`      | `PUT`       |
| `DestroyAPIView`    | Delete a single object using `pk`      | `DELETE`    |

#### Examples:

```python
# List all employees
class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Create a new employee
class EmployeeCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Retrieve a single employee by pk
class EmployeeRetrieve(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Update a single employee by pk
class EmployeeUpdate(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Delete a single employee by pk
class EmployeeDelete(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
```

---

### 🔗 Combined Generic Views (Multiple Operations)

| Generic View                    | Operations                          | HTTP Methods         |
|---------------------------------|-------------------------------------|----------------------|
| `ListCreateAPIView`            | List + Create                       | `GET`, `POST`        |
| `RetrieveUpdateAPIView`        | Retrieve + Update                   | `GET`, `PUT`         |
| `RetrieveDestroyAPIView`       | Retrieve + Delete                   | `GET`, `DELETE`      |
| `RetrieveUpdateDestroyAPIView` | Retrieve + Update + Delete          | `GET`, `PUT`, `DELETE`|

#### Examples:

```python
# List all employees & Create a new employee
class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Retrieve & Update a single employee
class EmployeeRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Retrieve, Update & Delete a single employee
class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
```

---

### 🏗️ How It All Connects

```
Level 1: APIView (Manual - Write Everything)
   ↓
Level 2: GenericAPIView + Mixins (Semi-Automatic)
   ↓
Level 3: Generics (Fully Automatic - Least Code) ✅
```

| Level   | Approach              | Code Required | Flexibility |
|---------|-----------------------|---------------|-------------|
| Level 1 | `APIView`             | Most          | Most        |
| Level 2 | `Mixins + GenericAPIView` | Medium    | Medium      |
| Level 3 | `Generics`            | Least         | Least       |

---

### 🎯 When to Use What?

| Use Case                                    | Best Choice       |
|---------------------------------------------|--------------------|
| Need full control over logic                | `APIView`          |
| Need some customization with reusable code  | `Mixins`           |
| Standard CRUD with minimal code             | `Generics` ✅      |

---

### 📌 URL Configuration Example

```python
from django.urls import path
from .views import EmployeeListCreate, EmployeeRetrieveUpdateDestroy

urlpatterns = [
    path('employees/', EmployeeListCreate.as_view()),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view()),
]
```

> With just **2 views** and **2 URLs**, you get full **CRUD** functionality! 🚀