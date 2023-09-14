from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


class IndexClass(View):
    def get(self,req):
        return render(req, 'login/login.html',{})
    
    def post(self,req):
        username=req.POST.get('username')
        password=req.POST.get('password')
        return HttpResponse(f'KQ: username: {username},pass: {password}')
