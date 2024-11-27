from django.shortcuts import render, get_object_or_404, redirect
from .forms import ImageUploadForm
from .models import Image

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Сохраняем изображение в базе данных
            image = form.save()
            # Передаем ID изображения в контекст
            return render(request, 'image_upload/upload_success.html', {'image': image})
    else:
        form = ImageUploadForm()
    return render(request, 'image_upload/upload_image.html', {'form': form})

def view_image(request, id):
    # Получаем изображение по ID, если оно существует, или возвращаем 404
    image = get_object_or_404(Image, id=id)
    return render(request, 'image_upload/view_image.html', {'image': image})

def list_images(request):
    # Получаем все изображения из базы данных
    images = Image.objects.all()
    return render(request, 'image_upload/list_images.html', {'images': images})

def delete_image(request, id):
    # Получаем изображение по ID
    image = get_object_or_404(Image, id=id)

    # Удаляем изображение
    if request.method == 'POST':
        image.delete()
        return redirect('list_images')  # После удаления переходим обратно на страницу со списком изображений

    return render(request, 'image_upload/confirm_delete.html', {'image': image})
