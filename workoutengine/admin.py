from django.contrib import admin
from .models import Exercicio, Treino, ItemTreino

# Register your models here.

@admin.register(Exercicio)
class ExerciciosAdmin(admin.ModelAdmin):
    list_display = ('name', 'muscle_group', 'difficulty')
    list_filter = ('muscle_group', 'difficulty')
    search_fields = ('name',)

class WorkoutItemInline(admin.TabularInline):
    model = ItemTreino
    extra = 1 # Quantos campos vazios aparecem por padrão

@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal', 'name', 'created_at')
    list_filter = ('goal', 'user')
    search_fields = ('user__username', 'name')

# @admin.register(TreinoExercicio)
# class TreinoExercicioAdmin(admin.ModelAdmin):
#     list_display = ('treino', 'exercicio', 'order')
#     list_filter = ('treino__goal',)
#     search_fields = ('treino__user__username', 'exercicio__name')