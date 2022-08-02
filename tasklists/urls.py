from django.urls import path

from  .import views

app_name = 'tasklists'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:task_id>', views.details, name="details"),
    path('add', views.create_view, name="create_view"),
    path('edit/<id>', views.profile, name="update"),
    path('profile/<id>', views.profile, name="profile")
]