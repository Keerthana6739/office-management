from django.urls import path,include
from sub_part import views

urlpatterns=[
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('dashboard',views.dashboard,name='dashboard'),
    

]