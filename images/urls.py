from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import ImageViewSet

urlpatterns = [
    path("", ImageViewSet.as_view(), name="image_list"),
    path('upload', ImageViewSet.as_view(), name='upload-file'),
]+static(settings.STATIC_URL,
         document_root=settings.STATIC_ROOT
         )+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
