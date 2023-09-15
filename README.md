# .vscode/settings.json

```json
  "emmet.includeLanguages": {
    "css": "css",
    "html": "html",
    "scss": "scss",
    "javascript": "javascriptreact",
    "django-html": "html"
  },
  "emmet.useInlineCompletions": true,
  "files.associations": {
    "*html": "html",
    "*css": "css",
    "*scss": "scss",
    "**/*.html":"html",
    "**/templates/**/*.html":"django-html",
    "**/templates/**/*":"django-txt",
  },
  "python.pythonPath":"/usr/local/bin/python3",
  "python.languageServer":"Pylance",
```

# cai dat goi python3 truoc

```python
pip install django
```

# Tao project

```python
django-admin startproject site1
```

# tao app co 2 cach

```commandline
python manage.py startapp [name]
```

```commandline
django-admin startapp app1
django-admin startapp [name]
```

# chay trong site1

- Dung django khoi tao html co ban trong [site1]

```
cd site1
python3 manage.py migrate
```

1. run server 'host-ao'

```commandline
 python3 manage.py runserver 8888
```

2. tao user admin

```commandline
python3 manage.py createsuperuser
```

- nhap thoi
  vd:
  user:tien
  pass: 1234

3. vao link cua admin
   http://127.0.0.1:8888/admin
4. tao module - tao app [home]

```commandline
python manage.py startapp [name]
python manage.py startapp home
```

# tai folder [home]

1. tao folder [Templates] > file [home.html]

# quay lai site1

1. site1/site1/setting.py

- them vao INSTALLED_APPS =[
  ...,
  'home'
  ]

2. site1/home/view.py

- them vao:

```commandline
def get_home(req):
    return render(req,'home.html')
```

3. site1/site1/urls:

- from home import views as home
- path('',home.get_home)

```
from django.contrib import admin
from django.urls import path
from home import views as home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.get_home)
]
```

4. migrate lai >run

```
python manage.py migrate
```

# ket noi Mysql

5. cai dat xampp
6. ...setting.py

- dat lenh cho DTB

```commandline

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'site1',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
         'PORT':'3307'
    }
}
```

7. cai pip mysql

```commandline
pip install pymysql
```

8. migrate > run
9. error
   **init**.py

```commandline
import pymysql
pymysql.install_as_MySQLdb()
```

- update pip

# Dang ky Model vao trang .../admin

app/admin.py

```
from django.contrib import admin
from .models import Question,Choice
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
```

# tao **str** thay doi hien thi model trong admin page

```python
class Post(models.Model):
    title= models.CharField(max_length=100)
    content= models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title
```

# static img

```python
python manage.py collectstatic
```

html:

- load static

```python
{% load static %}
```

html:

```django
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Home</title>
  </head>
  <body>
    <img src="{% static "login/images/ava.jpeg" %} " alt="">
  </body>
</html>
```
