from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('detail/<int:member_id>/', views.detail, name='detail'),
    path('edit/<int:member_id>/', views.edit, name='edit'),

]