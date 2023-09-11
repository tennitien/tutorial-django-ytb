from django.http import HttpResponse
# Create your views here.
def index(req):
    return HttpResponse('This is app 1')
def child(req):
    return HttpResponse('child app')