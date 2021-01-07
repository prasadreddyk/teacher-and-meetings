from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('teachersDetails',views.teachersDetails, name='teachersDetails'),
    path('data', views.mail, name='mail'),
    path('send', views.sendmail, name='email'),
    path('oneteachers', views.oneTeacher, name='oneteacher'),
]