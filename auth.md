# xac thuc user da dan nhap chua:

- gioi han nguoi dung

```python
from django.views import View
from django.contrib.auth import authenticate,login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin

# Cach 1:
class ViewUser(View):
    def get(self,req):
        if not req.user.is_authenticated:
            return HttpResponse('Vui long dang nhap')
        else:
            return HttpResponse('Ban da dang nhap r')

# Cach 2: ngan hon

@decorators.login_required(login_url='/login/')
def view_product(req):
    return HttpResponse('decor')

# Cach 3: tot nhat
class LoginRequire(LoginRequiredMixin, View):
    login_url='/login/'
    def get(self,req):
        return HttpResponse('Ban da dang nhap r')
```

- urls:

```python

urlpatterns = [
    path('login/',views.IndexClass.as_view(),name='index'),
    path('user/',views.ViewUser.as_view(),name='user'),
    path('view/',views.view_product,name='view'),
    path('required/',views.LoginRequire.as_view(),name='Required'),
]
```
