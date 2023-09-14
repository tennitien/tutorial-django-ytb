from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate,login
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
    

class ViewUser(View):
    def get(self,req):
        if not req.user.is_authenticated:
            return HttpResponse('Vui long dang nhap')
        else:
            return HttpResponse('Ban da dang nhap r')
        