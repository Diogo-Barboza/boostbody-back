from django.contrib import admin
from .models import Exercicio

# Register your models here.

@admin.register(Exercicio)
class ExerciciosAdmin(admin.ModelAdmin):
    list_display = ('name', 'muscle_group', 'difficulty')
    list_filter = ('muscle_group', 'difficulty')
    search_fields = ('name',)