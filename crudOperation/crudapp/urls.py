from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.getcreate, name='create'),
    path('update/<int:id>', views.getupdate, name='update'),
    path('delete/<int:id>', views.getdelete, name='delete'),
    path('confirmdelete/<int:id>', views.getConfirmDelete, name='confirmdelete')
]
