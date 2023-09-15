# tao bien o views & html:

../html

```
   <h1>Toi ten la: {{name}}</h1>
```

views.py

```
def index(req):
    myname='Tien ichii'
    context={'name':myname}
    return render(req,'home.html',context)
```

# for in & if:

html

```
<ul>
      {% for item in list %}
        {% if item != 'html' %}
        <li>{{item}}</li>
        {% endif %}
      {% endfor %}
    </ul>
```

views:

```
def index(req):
    myname='Tien ichii'
    list=['js','java','python','html']
    context={'name':myname, 'list':list}
    return render(req,'home.html',context)
    # return render(req,'home.html',{})
```

# extend , block:

base.html

- vi tri block la noi chen main-content(home.html)

```
 {% block content %}{% endblock %}
 {% block [nameXY] %}{% endblock %}
```

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <nav>Navbar</nav>
    {% block content %}{% endblock %}
    <footer>Footer</footer>
  </body>
</html>

```

home.html

- name trong block giong nhau
- extends : thu muc goc la templates

```
{% extends 'base.html' %} {% block content %}
```

```
{% extends 'base.html' %} {% block content %}
<h3>Toi ten la: {{name}}</h3>
<h4>Language IT:</h4>
<ul>
  {% for item in list %} {% if item != 'html' %}
  <li>{{item}}</li>
  {% endif %} {% endfor %}
</ul>
{% endblock %}

```

# lay thu muc goc la folder [templates]

- views.py
- \*_/_.html

# model many

## model ex:

```
from django.db import models

# Create your models here.
class Question(models.Model):
    question=models.CharField(max_length=200)
    time=models.DateTimeField()

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice=models.CharField(max_length=200)
    vote=models.IntegerField(default=0)
```

## views:

- lay id

```
Question.objects.get(pk=question_id)
```

```
def detailView(req, question_id):
    q= Question.objects.get(pk=question_id)
    context={'question':q}
    return render(req,'detail_question.html',context)
```

## html

- goi toi model khac co khoa forgeinkey -> ten class viet thuong + \_set

```python
{% for item in question.choice_set.all %}
```

```python
{% for item in question.choice_set.all %}
  {{item.choice}}
{% endfor %}
```

## urls

- def name_id phai giong vs | path

```python
def detailView(req, question_id):
____
path('detail/<int:question_id>',views.detailView, name='detail')

```

```python
urlpatterns = [
    path('', views.index, name='index'),
    path('list/',views.viewlist, name='list'),
    path('detail/<int:question_id>',views.detailView, name='detail')
]
```

# a href

### url detail == name da khai bao o urls.py

- html

```python
<a href="{% url "detail" item.id %}">{{item.question}}</a>
```

- urls.py

```python
path('detail/<int:question_id>',views.detailView, name='detail')
```

# model && form

model:

```python
class Post(models.Model):
    title= models.CharField(max_length=100)
    content= models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title
```

form:

- cau truc dien hinh phai co du: Meta= mac dinh ko doi ten

```python
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model= Post
        fields= ['title','content']
```

html:

- url = name : trong urls.py
- token: bat buoc
- {fm} : bien trong formModel

```python
<form action="{% url "add-post" %}" method="post">
        {% csrf_token %}
        {{fm}}
        <input type="submit" value="Add">
</form>
```

views:

- get: de hien thi
- post: nhan du lieu
- f.save(): phai co moi luu vao db

```python
class AddPost(View):
    def get(self,req):
        f= PostForm()
        context={'fm':f}
        return render(req, 'login/add_post.html',context)

    def post(self,req):
        f= PostForm(req.POST) # nhan du lieu
        if not f.is_valid():  # check
            return HttpResponse('nhap sai')
        f.save() # luu vao database
        return HttpResponse('ok')

```
