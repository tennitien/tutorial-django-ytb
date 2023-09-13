from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
 
# Create your views here.
# thu muc goc tro tu folder template
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

def detailView(req, question_id):
    q=Question.objects.get(pk=question_id)
    context={'question':q}
    return render(req,'detail_question.html',context)

def votePost(req,question_id):
    # q= Question.objects.get(question_id)
    data=req.POST('choice')
     #choice = input
    return HttpResponse('choice')