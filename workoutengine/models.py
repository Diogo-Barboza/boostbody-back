from django.db import models
from django.conf import settings

# Create your models here.

class Exercicio(models.Model):

    MUSCLE_GROUPS_CHOICES = [
        ('ches_upper', 'Peito (Superior)'),
        ('chest_lower', 'Peito (Inferior)'),
        ('chest_middle', 'Peito (Médio)'),
        ('back_upper', 'Costas (Parte Superior)'),
        ('back_lats', 'Costas (Grande Dorsal)'),
        ('back_middle', 'Costas (Miolo)'),
        ('back_lower', 'Costas (Parte Inferior)'),
        ('legs_quads', 'Pernas (Quadríceps)'),
        ('legs_hamstrings', 'Pernas (Posterior)'),
        ('legs_glutes', 'Pernas (Glúteos)'),
        ('legs_calves', 'Pernas (Panturrilhas)'),
        ('shoulders_ant', 'Ombros (Anterior)'),
        ('shoulders_med', 'Ombros (Médio)'),
        ('shoulders_post', 'Ombros (Posterior)'),
        ('biceps_long', 'Bíceps (Cabeça Longa)'),
        ('biceps_short', 'Bíceps (Cabeça Curta)'),
        ('triceps_long', 'Tríceps (Cabeça Longa)'),
        ('triceps_middle', 'Tríceps (Cabeça Medial)'),
        ('triceps_lat', 'Tríceps (Cabeça Lateral)'),

        ('abs', 'Abdômen'),
    ]

    DIFFICULTY_CHOICES = [
        (1, 'Iniciante'),
        (2, 'Intermediário'),
        (3, 'Avançado'),
    ]

    name = models.CharField(max_length=100, unique=True)
    muscle_group = models.CharField(max_length=20, choices=MUSCLE_GROUPS_CHOICES)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=1)
    description = models.TextField(blank=True, help_text="Breve descrição de como executar.")
    video_url = models.URLField(blank=True, null=True, help_text="Link para um vídeo demonstrativo do exercício.")

    # Meta class to define ordering and verbose names
    class Meta:
        verbose_name = "Exercício"
        verbose_name_plural = "Exercícios"

    def __str__(self):
        return f"{self.name} - {self.get_muscle_group_display()}"
    
class Treino(models.Model):
    GOAL_CHOICES = [
        ('hipertrofia', 'Hipertrofia'),
        ('resistencia', 'Resistência'),
        ('forca', 'Força'),
        ('emagrecimento', 'Emagrecimento'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Nome do Treino")
    created_at = models.DateTimeField(auto_now_add=True)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES, verbose_name="Objetivo do Treino", default='hipertrofia')

    class Meta:
        verbose_name = "Treino"
        verbose_name_plural = "Treinos"

    def __str__(self):
        return f"{self.name} - {self.user.email}"
        
class ItemTreino(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE, related_name='itens')
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest_time = models.IntegerField(help_text="Tempo de descanso entre as séries (em segundos)")

    class Meta:
        verbose_name = "Item de Treino"
        verbose_name_plural = "Itens de Treino"

    def __str__(self):
        return f"{self.exercicio.name} - {self.sets}x{self.reps} (Descanso: {self.rest_time}s)"