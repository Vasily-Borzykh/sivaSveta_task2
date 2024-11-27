from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('image/<int:id>/', views.view_image, name='view_image'),
    path('image/<int:id>/delete/', views.delete_image, name='delete_image'),  # Путь для удаления изображения
    path('', views.list_images, name='list_images'),  # Путь для списка изображений
]
