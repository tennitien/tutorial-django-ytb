from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexClass.as_view(), name='index'),
    path('add/', views.addPost, name='add'),
    # path('save/', views.save_news, name='save'),
    path('save/', views.SaveNewClass.as_view(), name='save'),
    path('email/', views.email_view, name='email'),
    path('process/', views.process, name='process'),
]
