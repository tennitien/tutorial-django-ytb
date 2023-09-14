from django.urls import path
from . import views


urlpatterns = [
    path('',views.IndexClass.as_view(),name='index'),
    path('user/',views.ViewUser.as_view(),name='user'),
]