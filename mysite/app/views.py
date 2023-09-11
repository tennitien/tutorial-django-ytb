from django.shortcuts import render
from .models import Question
# Create your views here.
def index(req):
    myname='Tien ichii'
    list=['js','java','python','html']
    context={'name':myname, 'list':list}
    return render(req,'home.html',context)
    # return render(req,'home.html',{})

def viewlist(req):
    list_question=Question.objects.all()
    context={'list': list_question}
    return render(req,'questions_list.html',context)