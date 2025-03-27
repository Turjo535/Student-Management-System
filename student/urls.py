from django.urls import path
from .views import display_student,add_student,update_student,delete

urlpatterns = [
    path('',display_student,name="home"),
    path('add/',add_student,name="add"),
    path('update/<int:id>',update_student,name="update"),
    path('delete/<int:id>',delete,name="delete"),
]
