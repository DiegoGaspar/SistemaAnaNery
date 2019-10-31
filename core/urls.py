from django.conf.urls import url, include
from .views import (
    home,
    aluno_novo,
    lista_alunos,
    aluno_update,
    aluno_delete,
    confirmacao_cadastro,
    lista_professor,
    professor_novo,
    professor_update,
    professor_delete,
    lista_cursos,
    curso_novo,
    curso_update,
    curso_delete,
)


urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^confirmacao/$', confirmacao_cadastro, name='core_confirmacao_cadastro'),

    url(r'^alunos/$', lista_alunos, name='core_lista_alunos'),
    url(r'^cadastro-aluno/$', aluno_novo, name='core_aluno_novo'),
    url(r'^aluno-update/(?P<id>\d+)/$', aluno_update, name='core_aluno_update'),
    url(r'^aluno-delete/(?P<id>\d+)/$', aluno_delete, name='core_aluno_delete'),

    url(r'^professor/$', lista_professor, name='core_lista_professor'),
    url(r'^cadastro-professor/$', professor_novo, name='core_professor_novo'),
    url(r'^professor-update/(?P<id>\d+)/$', professor_update, name='core_professor_update'),
    url(r'^professor-delete/(?P<id>\d+)/$', professor_delete, name='core_professor_delete'),

    url(r'^cursos/$', lista_cursos, name='core_lista_cursos'),
    url(r'^cadastro-curso/$', curso_novo, name='core_curso_novo'),
    url(r'^curso-update/(?P<id>\d+)/$', curso_update, name='core_curso_update'),
    url(r'^curso-delete/(?P<id>\d+)/$', curso_delete, name='core_curso_delete'),

]




