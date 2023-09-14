from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.IndexClass.as_view(),name='index'),
    path('user/',views.ViewUser.as_view(),name='user'),
    path('view/',views.view_product,name='view'),
    path('required/',views.LoginRequire.as_view(),name='Required'),
]