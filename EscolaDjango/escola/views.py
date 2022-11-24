from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaMatriculadosCursoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunosViewSet(viewsets.ModelViewSet):
    """ exibindo todos os alunos e alunas """

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """ exibindo todos os cursos """

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    """ listando todas as matriculas """

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasAluno(generics.ListAPIView):
    """ listando as matriculas de um aluno(a) """

    def get_queryset(self):
        query_set = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return query_set
    serializer_class = ListaMatriculasAlunoSerializer


class ListaMatriculadosCurso(generics.ListAPIView):
    """ listando os alunos matriculados em um curso """

    def get_queryset(self):
        query_set = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return query_set
    serializer_class = ListaMatriculadosCursoSerializer