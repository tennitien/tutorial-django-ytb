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
