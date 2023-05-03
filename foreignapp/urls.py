from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name="home"),
    path('add_course',views.add_course,name="add_course"),
    path('add_coursedb',views.add_coursedb,name="add_coursedb"),
    path('add_student',views.add_student,name="add_student"),
    path('add_studentdb',views.add_studentdb,name="add_studentdb"),
    path('show_details',views.show_details,name="show_details"),
    path('editpage/<int:pk>',views.editpage,name="editpage"),
    path('edit_student_details/<int:pk>',views.edit_student_details,name="edit_student_details"),
    path('edit_details',views.edit_details,name="edit_details"),
    path('deletepage/<int:pk>',views.deletepage,name="deletepage")
         
  

]