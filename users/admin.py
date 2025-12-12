from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

# Register your models here.

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoaos', {'fields': ('first_name', 'last_name', 'data_nascimento', 'altura', 'peso', 'acad_experiencia')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    ordering = ('email'),
    search_fields = ('email', )

admin.site.register(User, CustomUserAdmin)