from django.urls import re_path

from app import views

urlpatterns = [

    
    re_path(r'^$', views.index, name='index'),
    re_path(r'^upcoming$', views.upcoming, name='upcoming'),
    re_path(r'^tasks$', views.tasks, name='tasks'),
    re_path(r'^viewprojectform$', views.viewprojectform, name='viewprojectform'),
    re_path(r'^acceptedprojects$', views.acceptedprojects, name='acceptedprojects'),
    re_path(r'^rejected$', views.rejected, name='rejected'),
    re_path(r'^givetask$', views.givetask, name='givetask'),
    re_path(r'^currenttasks$', views.currenttasks, name='currenttasks'),
    re_path(r'^previoustasks$', views.previoustasks, name='previoustasks'),
    
    


    

]