from django.urls import path
from . import views


app_name='app'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/',views.viewlist, name='list'),
    path('detail/<int:question_id>',views.detailView, name='detail'),
    # path('<int:question_id>',views.votePost, name='votePost'),
] 