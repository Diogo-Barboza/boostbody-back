from django.contrib.auth.base_user import BaseUserManager

## Usado para ignorar username (campo que o Django usa)

class CustomUserManager(BaseUserManager):
    # Sobrescreve create_user para aceitar email como campo principal
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(('O Email deve ser configurado'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # Sobrescreve create_superuser para aceitar email como campo principal
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
            
        return self.create_user(email, password, **extra_fields)