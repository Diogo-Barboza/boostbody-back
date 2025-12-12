from rest_framework import serializers
from . import User

class RegistroUsuario(serializers.ModelSerializer):
    ## Write only para nao retornar na resposta
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'nome',
            'dataNascimento',
            'altura',
            'peso',
            'tempoExperiencia'
        )

        read_only_fields = ('id', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            name = validated_data.get('nome', ''),
            data_nascimento = validated_data.get('dataNascimento'),
            altura = validated_data.get('altura'),
            peso = validated_data.get('peso'),
            acad_experiencia = validated_data.get('tempoExperiencia', 0.0),
        )

        return user
