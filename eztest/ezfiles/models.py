from django.db import models
from django.core.exceptions import ValidationError
from users.models import User
import uuid
import os


# Create your models here.


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pptx', '.docx', '.xlsx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('You can only upload pptx, docx and xlsx files.')

class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    file = models.FileField(upload_to='uploads/', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
