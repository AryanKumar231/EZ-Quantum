from django.urls import path
from .views import FileUploadView, FileListView, FileDownloadView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('upload-file/', FileUploadView.as_view(), name='file-upload'),
    path('list-files/', FileListView.as_view(), name='file-list'),
    path('download-file/<uuid:uuid>/', FileDownloadView.as_view(), name='file-download'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)