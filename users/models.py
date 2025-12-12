from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.

class User(AbstractUser):
    # email como campo de login
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'

    username = None
    objects = CustomUserManager()
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [] # email e senha já são obrigatórios

    altura = models.IntegerField(
        verbose_name = "Altura (cm)",
        null = True,
        blank = True
    )

    peso = models.DecimalField(
        verbose_name = "Peso (kg)",
        max_digits = 5,
        decimal_places = 2,
        null = True,
        blank = True
    )

    acad_experiencia = models.DecimalField(
        verbose_name = "Anos de Experiência na Academia",
        max_digits = 3,
        decimal_places = 1,
        default = 0.0
    )

    data_nascimento = models.DateField(
        verbose_name = "Data de Nascimento",
        null = True,
        blank = True 
    )


    def __str__(self):
        return self.email