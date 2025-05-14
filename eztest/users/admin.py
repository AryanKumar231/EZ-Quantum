from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'role', 'is_active', 'is_admin','is_verified')
    search_fields = ('email',)
    list_filter = ('role',)
    ordering = ('-created_at',)
    list_editable = ('is_active','role')
    
admin.site.register(User, UserAdmin)