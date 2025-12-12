from rest_framework import serializers
from .models import User

class RegistroUsuario(serializers.ModelSerializer):
    ## Write only para nao retornar na resposta
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'password',
            'data_nascimento',
            'altura',
            'peso',
            'acad_experiencia'
        )

        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            first_name = validated_data.get('first_name', ''),
            last_name = validated_data.get('last_name', ''),
            data_nascimento = validated_data.get('dataNascimento'),
            altura = validated_data.get('altura'),
            peso = validated_data.get('peso'),
            acad_experiencia = validated_data.get('tempoExperiencia', 0.0),
        )

        return user
