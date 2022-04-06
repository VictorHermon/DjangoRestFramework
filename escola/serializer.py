from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')
    cpf = serializers.ReadOnlyField(source='aluno.cpf')
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        exclude = []

    def get_periodo(self, nome_periodo):
        return nome_periodo.get_periodo_display()


class MatriculasDoAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, nome_periodo):
        return nome_periodo.get_periodo_display()


class MatriculasNoCursoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    aluno_cpf = serializers.ReadOnlyField(source='aluno.cpf')

    class Meta:
        model = Matricula
        fields = ['aluno_nome', 'aluno_cpf']
