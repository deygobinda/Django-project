from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.hello_view),
    path('userform/',views.userdata,name='userform'),
    path('signin/',views.signin,name='singin'),
    path('calculator/',views.calculator),
    path('',views.landing , name="landing"),
    path('userdatafetch/',views.fetchuseralldata , name="fetchusers"),
    path('userdataupdate/<int:x>/', views.userdataupdate, name='userdataupdata'),
    path('deleteuser/<int:x>/', views.deleteUser, name='deleteuser')
]
