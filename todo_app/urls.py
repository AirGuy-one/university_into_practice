from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('del/<str:item_id>', views.remove, name="del"),
]
