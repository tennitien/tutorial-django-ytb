from django.shortcuts import render
from django.http import HttpResponse
from .form import PostForm, SendMail
from django.views import View
# Create your views here.


class IndexClass(View):
    def get(self, req):
        return HttpResponse('Class')


def addPost(req):
    form = PostForm()
    context = {'f': form}
    return render(req, 'news/add_news.html', context)


# def save_news(req):
#     if req.method == 'POST':
#         q = PostForm(req.POST)

#         if q.is_valid():
#             q.save()
#             return HttpResponse('luu')
#         else:
#             return HttpResponse('khong luuu')
# chuyen sang Classviews
class SaveNewClass(View):
    # nhan data from add-form
    def post(self, req):
        q = PostForm(req.POST)
        if q.is_valid():
            q.save()
            return HttpResponse('luu')
        else:
            return HttpResponse('khong luuu')

    def get(self, req):
        form = PostForm()
        context = {'f': form}
        return render(req, 'news/add_news.html', context)


def email_view(req):
    b = SendMail()
    return render(req, 'news/email.html', {'f': b})


def process(req):
    if req.method == 'POST':
        m = SendMail(req.POST)
        if m.is_valid():
            tieude = m.cleaned_data['title']
            email = m.cleaned_data['email']
            noidung = m.cleaned_data['content']
            cc = m.cleaned_data['cc']
            context1 = {'tieude': tieude, 'email': email,
                        'noidung': noidung, 'cc': cc}

            context2 = {'data': m}
            return render(req, 'news/print_email.html', context2)
