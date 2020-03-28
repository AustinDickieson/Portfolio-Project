from django.urls import path

from . import views #pull from views.py in blog

urlpatterns = [
    path('', views.allblogs, name='allblogs'),#making the job views the home page
    path('<int:blog_id>/', views.detail, name='detail')#look for int after blog and save as blog id
]
