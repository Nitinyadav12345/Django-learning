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


## 📖 ViewSets in Django REST Framework

ViewSets are the **highest level of abstraction** in Django REST Framework. They combine the logic for **multiple related views** into a **single class**, reducing code even further than generics.

Instead of writing separate views for `list`, `create`, `retrieve`, `update`, and `delete`, ViewSets handle **all of them in one place**.

---

### 🏗️ How It All Connects

```
Level 1: APIView (Manual - Write Everything)
   ↓
Level 2: GenericAPIView + Mixins (Semi-Automatic)
   ↓
Level 3: Generics (Automatic)
   ↓
Level 4: ViewSets (Most Automatic - Least Code) ✅
```

---

### 1️⃣ `viewsets.ViewSet`

A basic ViewSet where you **manually define** the logic for each action.

| Method       | Operation                           | HTTP Method |
|--------------|-------------------------------------|-------------|
| `list()`     | Get all objects                     | `GET`       |
| `create()`   | Create a new object                 | `POST`      |
| `retrieve()` | Get a single object using `pk`      | `GET`       |
| `update()`   | Update a single object using `pk`   | `PUT`       |
| `destroy()`  | Delete a single object using `pk`   | `DELETE`    |

#### Example:

```python
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def update(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response(status=204)
```

---

### 2️⃣ `viewsets.ModelViewSet`

The **most powerful and simplest** ViewSet. It takes only `queryset` and `serializer_class` and **automatically provides all CRUD operations** — both pk-based and non-pk-based.

#### Example:

```python
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
```

> ✅ **That's it!** Just **2 lines** and you get full CRUD functionality!

#### What It Automatically Provides:

| Operation                        | HTTP Method | URL Example              |
|----------------------------------|-------------|--------------------------|
| List all employees               | `GET`       | `/employees/`            |
| Create a new employee            | `POST`      | `/employees/`            |
| Retrieve a single employee       | `GET`       | `/employees/1/`          |
| Update a single employee         | `PUT`       | `/employees/1/`          |
| Partial update a single employee | `PATCH`     | `/employees/1/`          |
| Delete a single employee         | `DELETE`    | `/employees/1/`          |

---

### 🔄 Comparison: ViewSet vs ModelViewSet

| Feature                | `viewsets.ViewSet`         | `viewsets.ModelViewSet`    |
|------------------------|----------------------------|---------------------------|
| Code Required          | More (manual logic)        | Least (automatic) ✅      |
| Define queryset        | Manually in each method    | Once at class level        |
| Define serializer      | Manually in each method    | Once at class level        |
| CRUD Operations        | Write each method yourself | Auto-generated             |
| Flexibility            | More                       | Less                       |
| Best For               | Custom logic               | Standard CRUD ✅           |

---

### 📌 URL Configuration with Router

ViewSets use **Routers** instead of manually defining URL patterns. The router **automatically generates** all the required URLs.

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

#### URLs Auto-Generated by Router:

| URL                    | HTTP Method | Operation          |
|------------------------|-------------|--------------------|
| `/employees/`          | `GET`       | List all           |
| `/employees/`          | `POST`      | Create             |
| `/employees/1/`        | `GET`       | Retrieve (pk=1)    |
| `/employees/1/`        | `PUT`       | Update (pk=1)      |
| `/employees/1/`        | `PATCH`     | Partial Update     |
| `/employees/1/`        | `DELETE`    | Delete (pk=1)      |

---

### 🎯 Complete Comparison: All Levels

| Level   | Approach                    | Code Required | Flexibility | Best For            |
|---------|-----------------------------|---------------|-------------|---------------------|
| Level 1 | `APIView`                   | Most          | Most        | Full custom logic   |
| Level 2 | `Mixins + GenericAPIView`   | Medium        | Medium      | Reusable components |
| Level 3 | `Generics`                  | Less          | Less        | Standard views      |
| Level 4 | `ViewSet`                   | Less          | Medium      | Custom ViewSets     |
| Level 5 | `ModelViewSet`              | Least ✅      | Least       | Standard CRUD ✅    |

---

### 💡 Summary

```
APIView          → Write everything manually
Mixins           → Reusable pieces + GenericAPIView
Generics         → Pre-built views (ListCreateAPIView, etc.)
ViewSet          → All actions in one class (manual logic)
ModelViewSet     → All actions in one class (automatic) 🚀
```

> 🚀 **ModelViewSet** = `queryset` + `serializer_class` = **Full CRUD in 2 lines!**

---

Here is the **raw README.md** text:

````
## 📖 ViewSets in Django REST Framework

ViewSets are the **highest level of abstraction** in Django REST Framework. They combine the logic for **multiple related views** into a **single class**, reducing code even further than generics.

Instead of writing separate views for `list`, `create`, `retrieve`, `update`, and `delete`, ViewSets handle **all of them in one place**.

---

### 🏗️ How It All Connects

```
Level 1: APIView (Manual - Write Everything)
   ↓
Level 2: GenericAPIView + Mixins (Semi-Automatic)
   ↓
Level 3: Generics (Automatic)
   ↓
Level 4: ViewSets (Most Automatic - Least Code) ✅
```

---

### 1️⃣ `viewsets.ViewSet`

A basic ViewSet where you **manually define** the logic for each action.

| Method       | Operation                           | HTTP Method |
|--------------|-------------------------------------|-------------|
| `list()`     | Get all objects                     | `GET`       |
| `create()`   | Create a new object                 | `POST`      |
| `retrieve()` | Get a single object using `pk`      | `GET`       |
| `update()`   | Update a single object using `pk`   | `PUT`       |
| `destroy()`  | Delete a single object using `pk`   | `DELETE`    |

#### Example:

```python
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def update(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response(status=204)
```

---

### 2️⃣ `viewsets.ModelViewSet`

The **most powerful and simplest** ViewSet. It takes only `queryset` and `serializer_class` and **automatically provides all CRUD operations** — both pk-based and non-pk-based.

#### Example:

```python
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
```

> ✅ **That's it!** Just **2 lines** and you get full CRUD functionality!

#### What It Automatically Provides:

| Operation                        | HTTP Method | URL Example              |
|----------------------------------|-------------|--------------------------|
| List all employees               | `GET`       | `/employees/`            |
| Create a new employee            | `POST`      | `/employees/`            |
| Retrieve a single employee       | `GET`       | `/employees/1/`          |
| Update a single employee         | `PUT`       | `/employees/1/`          |
| Partial update a single employee | `PATCH`     | `/employees/1/`          |
| Delete a single employee         | `DELETE`    | `/employees/1/`          |

---

### 🔄 Comparison: ViewSet vs ModelViewSet

| Feature                | `viewsets.ViewSet`         | `viewsets.ModelViewSet`    |
|------------------------|----------------------------|---------------------------|
| Code Required          | More (manual logic)        | Least (automatic) ✅      |
| Define queryset        | Manually in each method    | Once at class level        |
| Define serializer      | Manually in each method    | Once at class level        |
| CRUD Operations        | Write each method yourself | Auto-generated             |
| Flexibility            | More                       | Less                       |
| Best For               | Custom logic               | Standard CRUD ✅           |

---

### 📌 URL Configuration with Router

ViewSets use **Routers** instead of manually defining URL patterns. The router **automatically generates** all the required URLs.

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

#### URLs Auto-Generated by Router:

| URL                    | HTTP Method | Operation          |
|------------------------|-------------|--------------------|
| `/employees/`          | `GET`       | List all           |
| `/employees/`          | `POST`      | Create             |
| `/employees/1/`        | `GET`       | Retrieve (pk=1)    |
| `/employees/1/`        | `PUT`       | Update (pk=1)      |
| `/employees/1/`        | `PATCH`     | Partial Update     |
| `/employees/1/`        | `DELETE`    | Delete (pk=1)      |

---

### 🎯 Complete Comparison: All Levels

| Level   | Approach                    | Code Required | Flexibility | Best For            |
|---------|-----------------------------|---------------|-------------|---------------------|
| Level 1 | `APIView`                   | Most          | Most        | Full custom logic   |
| Level 2 | `Mixins + GenericAPIView`   | Medium        | Medium      | Reusable components |
| Level 3 | `Generics`                  | Less          | Less        | Standard views      |
| Level 4 | `ViewSet`                   | Less          | Medium      | Custom ViewSets     |
| Level 5 | `ModelViewSet`              | Least ✅      | Least       | Standard CRUD ✅    |

---

### 💡 Summary

```
APIView          → Write everything manually
Mixins           → Reusable pieces + GenericAPIView
Generics         → Pre-built views (ListCreateAPIView, etc.)
ViewSet          → All actions in one class (manual logic)
ModelViewSet     → All actions in one class (automatic) 🚀
```

> 🚀 **ModelViewSet** = `queryset` + `serializer_class` = **Full CRUD in 2 lines!**
````
## 📖 Pagination in Django REST Framework

Pagination is used to **split large datasets** into smaller, manageable chunks. Instead of returning **all records at once**, pagination returns a **limited number of records per page**.

---

### Why Pagination?

```
Without Pagination:
GET /employees/ → Returns 10,000 records at once 😰 (Slow & Heavy)

With Pagination:
GET /employees/?page=1 → Returns 10 records ✅ (Fast & Light)
GET /employees/?page=2 → Returns next 10 records ✅
```

---

### 1️⃣ `PageNumberPagination`

Returns results based on a **page number**. You specify which **page** you want to see.

#### URL Format:
```
/blogs/?page=1    → Returns first 10 records
/blogs/?page=2    → Returns next 10 records
/blogs/?page=10   → Returns records 91-100
```

#### How It Works:

| Parameter   | Description                              |
|-------------|------------------------------------------|
| `page_size` | Number of items to display per page      |
| `page`      | The page number you want to fetch        |

#### Example:

```
page_size = 10

Page 1 → Records 1-10
Page 2 → Records 11-20
Page 3 → Records 21-30
...
Page 10 → Records 91-100
```

#### Setup:

**Option 1: Global Setting (settings.py)**
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

**Option 2: Custom Pagination Class**
```python
from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
```

**Use in View:**
```python
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer
from .pagination import MyPageNumberPagination

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = MyPageNumberPagination
```

#### Response Format:
```json
{
    "count": 100,
    "next": "http://127.0.0.1:8000/blogs/?page=2",
    "previous": null,
    "results": [
        { "id": 1, "title": "Blog 1" },
        { "id": 2, "title": "Blog 2" },
        { "id": 10, "title": "Blog 10" }
    ]
}
```

---

### 2️⃣ `LimitOffsetPagination`

Returns results based on **limit** and **offset** values. You control **how many items** to fetch and **from where** to start.

#### URL Format:
```
/blogs/?limit=10&offset=0     → Returns first 10 records (1-10)
/blogs/?limit=10&offset=10    → Returns next 10 records (11-20)
/blogs/?limit=10&offset=20    → Returns next 10 records (21-30)
/blogs/?limit=5&offset=0      → Returns first 5 records (1-5)
```

#### How It Works:

| Parameter | Description                                          |
|-----------|------------------------------------------------------|
| `limit`   | Controls how many items you want to see in a single page |
| `offset`  | Tells the API where to start fetching the items from     |

#### Visual Example:

```
Total Records: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

?limit=5&offset=0   → [1, 2, 3, 4, 5]        (Start from 0, get 5)
?limit=5&offset=5   → [6, 7, 8, 9, 10]       (Start from 5, get 5)
?limit=5&offset=10  → [11, 12, 13, 14, 15]   (Start from 10, get 5)
?limit=3&offset=0   → [1, 2, 3]              (Start from 0, get 3)
?limit=3&offset=6   → [7, 8, 9]              (Start from 6, get 3)
```

#### Setup:

**Option 1: Global Setting (settings.py)**
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}
```

**Option 2: Custom Pagination Class**
```python
from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100
```

**Use in View:**
```python
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer
from .pagination import MyLimitOffsetPagination

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = MyLimitOffsetPagination
```

#### Response Format:
```json
{
    "count": 100,
    "next": "http://127.0.0.1:8000/blogs/?limit=10&offset=10",
    "previous": null,
    "results": [
        { "id": 1, "title": "Blog 1" },
        { "id": 2, "title": "Blog 2" },
        { "id": 10, "title": "Blog 10" }
    ]
}
```

---

### 🔄 Comparison: PageNumberPagination vs LimitOffsetPagination

| Feature                  | `PageNumberPagination`         | `LimitOffsetPagination`             |
|--------------------------|--------------------------------|-------------------------------------|
| URL Format               | `?page=2`                      | `?limit=10&offset=10`              |
| Control Items Per Page   | Fixed `page_size`              | Dynamic via `limit` parameter       |
| Control Starting Point   | Automatic (based on page)      | Manual via `offset` parameter       |
| Flexibility              | Less                           | More ✅                             |
| Simplicity               | More ✅                        | Less                                |
| Best For                 | Simple pagination              | Advanced/Custom pagination          |

---

### 🎯 When to Use What?

| Use Case                                         | Best Choice                |
|--------------------------------------------------|----------------------------|
| Simple page-by-page navigation                   | `PageNumberPagination` ✅  |
| Need control over how many items & starting point | `LimitOffsetPagination` ✅ |
| Frontend like Google Search (Page 1, 2, 3...)    | `PageNumberPagination`     |
| Frontend like Infinite Scroll / Load More        | `LimitOffsetPagination`    |

## 📖 Filtering in Django REST Framework

Filtering allows you to **narrow down** the results returned by an API based on specific **conditions or criteria**. Instead of returning all records, filtering returns only the records that **match your query**.

---

### Why Filtering?

```
Without Filtering:
GET /employees/ → Returns ALL 10,000 employees 😰

With Filtering:
GET /employees/?department=IT → Returns only IT department employees ✅
GET /employees/?salary=50000 → Returns employees with salary 50000 ✅
```

---

### Types of Filtering in Django REST Framework

```
1️⃣ Basic Filtering (Manual)
2️⃣ DjangoFilterBackend (django-filter)
3️⃣ SearchFilter
4️⃣ OrderingFilter
```

---

### 1️⃣ Basic Filtering (Manual)

You manually override the `get_queryset()` method to filter data based on query parameters.

#### Example:

```python
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()

        # Get query parameters from URL
        department = self.request.query_params.get('department')
        salary = self.request.query_params.get('salary')

        # Apply filters if parameters exist
        if department:
            queryset = queryset.filter(department=department)
        if salary:
            queryset = queryset.filter(salary=salary)

        return queryset
```

#### URL Usage:
```
GET /employees/?department=IT
GET /employees/?salary=50000
GET /employees/?department=IT&salary=50000
```

> ⚠️ This works but requires **manual code** for every filter.

---

### 2️⃣ DjangoFilterBackend (django-filter) ✅ Recommended

A **powerful and automatic** way to add filtering. It uses the `django-filter` package.

#### Installation:
```bash
pip install django-filter
```

#### Add to settings.py:
```python
INSTALLED_APPS = [
    ...
    'django_filters',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
```

#### Example:

```python
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department', 'salary', 'city']
```

#### URL Usage:
```
GET /employees/?department=IT
GET /employees/?salary=50000
GET /employees/?city=Mumbai
GET /employees/?department=IT&city=Mumbai
```

> ✅ **No manual code needed!** Just define `filterset_fields` and it works automatically.

---

### 3️⃣ SearchFilter

Allows you to **search** across one or more fields using a **single search query**. It performs a **partial match** (contains) search.

#### Example:

```python
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'department', 'city']
```

#### URL Usage:
```
GET /employees/?search=John
GET /employees/?search=IT
GET /employees/?search=Mumbai
```

#### How Search Works:

```
search_fields = ['name', 'department', 'city']

GET /employees/?search=John

→ Searches "John" in ALL three fields:
  - name CONTAINS "John" OR
  - department CONTAINS "John" OR
  - city CONTAINS "John"
```

#### Search Field Prefixes:

| Prefix | Lookup    | Example                  | Description              |
|--------|-----------|--------------------------|--------------------------|
| (none) | `icontains` | `search_fields = ['name']`  | Case-insensitive contains |
| `^`    | `istartswith` | `search_fields = ['^name']` | Starts with              |
| `=`    | `iexact`    | `search_fields = ['=name']` | Exact match              |
| `@`    | `search`    | `search_fields = ['@name']` | Full-text search         |

#### Example with Prefixes:

```python
class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^name', '=department', 'city']
    # name → starts with
    # department → exact match
    # city → contains
```

---

### 4️⃣ OrderingFilter

Allows you to **sort/order** the results based on specific fields.

#### Example:

```python
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'salary', 'created_at']
    ordering = ['name']  # Default ordering
```

#### URL Usage:
```
GET /employees/?ordering=name           → A to Z (Ascending)
GET /employees/?ordering=-name          → Z to A (Descending)
GET /employees/?ordering=salary         → Lowest salary first
GET /employees/?ordering=-salary        → Highest salary first
GET /employees/?ordering=name,salary    → Sort by name, then salary
```

| URL Parameter          | Result                    |
|------------------------|---------------------------|
| `?ordering=name`       | Ascending (A → Z)        |
| `?ordering=-name`      | Descending (Z → A)       |
| `?ordering=salary`     | Lowest salary first       |
| `?ordering=-salary`    | Highest salary first      |
| `?ordering=name,salary`| Sort by name, then salary |

---

### 🔗 Using Multiple Filters Together

You can combine **all filters** in a single view!

#### Example:

```python
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['department', 'city']       # Exact filtering
    search_fields = ['name', 'department']           # Search
    ordering_fields = ['name', 'salary']             # Ordering
    ordering = ['name']                              # Default order
```

#### URL Usage:
```
GET /employees/?department=IT                          → Filter by department
GET /employees/?search=John                            → Search "John"
GET /employees/?ordering=-salary                       → Order by salary (high to low)
GET /employees/?department=IT&search=John&ordering=-salary  → All combined!
```

---

### 🔄 Comparison: All Filtering Methods

| Filter Type          | Purpose                    | URL Example                      | Automatic? |
|----------------------|----------------------------|----------------------------------|------------|
| Basic (Manual)       | Custom filtering           | `?department=IT`                 | ❌ Manual   |
| `DjangoFilterBackend`| Exact field filtering      | `?department=IT&city=Mumbai`     | ✅ Auto     |
| `SearchFilter`       | Search across fields       | `?search=John`                   | ✅ Auto     |
| `OrderingFilter`     | Sort/Order results         | `?ordering=-salary`              | ✅ Auto     |

---

### 🎯 When to Use What?

| Use Case                                      | Best Choice             |
|-----------------------------------------------|-------------------------|
| Filter by exact field values                  | `DjangoFilterBackend` ✅ |
| Search a keyword across multiple fields       | `SearchFilter` ✅        |
| Sort results by a specific field              | `OrderingFilter` ✅      |
| Need complex custom filtering logic           | Basic (Manual) Filtering |
| Need all features together                    | Combine all three! 🚀   |