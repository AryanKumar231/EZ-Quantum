from django.contrib import admin
from .models import UploadedFile

# Register your models here.
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'user','assignment_id')
    search_fields = ('file', 'user__email')
    
    
admin.site.register(UploadedFile, UploadedFileAdmin)