from django.urls import path, include
from . import views

app_name = 'todo_items'
urlpatterns = [
    path('add-item',views.add_item_view,name='add-item'),
    path('update-item/<str:id>',views.update_item_view,name='update-item'),
    path('delete-item/<str:id>',views.delete_item_view,name='delete-item')
]