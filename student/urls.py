from django.urls import path
from . import views 
urlpatterns = [
    path ('', views.login,name="login"),
    path ('regist/', views.regist,name="regist"),
]