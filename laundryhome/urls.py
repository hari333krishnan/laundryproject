from django.urls import path

from laundryhome import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
]