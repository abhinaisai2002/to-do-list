from django.urls import path, include
from . import views

urlpatterns = [
    path('add-item',views.add_item_view,name='add-item'),
    path('update-item',views.update_item_view,name='update-item')
]