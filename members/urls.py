from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:member_id>/', views.DetailView.as_view(), name='detail'),
    path('edit/<int:member_id>/', views.EditView.as_view(), name='edit'),

]