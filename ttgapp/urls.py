from django.urls import re_path
from ttgapp import views

urlpatterns=[
    re_path(r'^Admin$',views.AdminApi),
    re_path(r'^Admin/([0-9])+$',views.AdminApi)
    
] 