from django.urls import path
from . import views

app_name = "workorders"

urlpatterns = [

    path("", views.workorder_list, name="list"),

    path("add/", views.workorder_create, name="create"),

    path("<int:pk>/", views.workorder_detail, name="detail"),

    path("<int:pk>/edit/", views.workorder_update, name="update"),

    path("<int:pk>/delete/", views.workorder_delete, name="delete"),

]