from django.db import models

# Create your models here.

class Exercicio(models.Model):
    MUSCLE_GROUPS_CHOICES = [
        ('chest', 'Peito'),
        ('back', 'Costas'),
        ('legs', 'Pernas'),
        ('shoulders', 'Ombros'),
        ('biceps', 'Bíceps'),
        ('triceps', 'Tríceps'),
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