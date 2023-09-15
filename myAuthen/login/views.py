from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate,login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
# Create your views here.


class IndexClass(View):
    def get(self,req):
        return render(req, 'login/login.html',{})
    
    def post(self,req):
        username=req.POST.get('username')
        password=req.POST.get('password')
        my_user= authenticate(username=username,password=password)
        
        if my_user is None:
            return HttpResponse('not have user')
        
        login(req,my_user)
        return render(req, 'login/home.html')
    
# cach 1:
class ViewUser(View):
    def get(self,req):
        if not req.user.is_authenticated:
            return HttpResponse('Vui long dang nhap')
        else:
            return render(req,'login/home.html')
        

# cach 3:
class LoginRequire(LoginRequiredMixin, View):
    login_url='/login/'
    def get(self,req):
        return HttpResponse('Ban da dang nhap r')

# cach 2:
@decorators.login_required(login_url='/login/')
def view_product(req):
    return HttpResponse('decor')



class AddPost(LoginRequiredMixin,View):
    login_url='/login/'

    def get(self,req):
        f= PostForm()
        context={'fm':f}
        return render(req, 'login/add_post.html',context)
    
    def post(self,req):
        f= PostForm(req.POST)
        if not f.is_valid():
            return HttpResponse('nhap sai')
        f.save()
        return HttpResponse('ok')
