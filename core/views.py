from django.shortcuts import render,redirect
from .models import Aluno, Professor, Curso
from .forms import AlunoForm, ProfessorForm, CursoForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {'mensagem':'Bem Vindo ao Curso Ana Nery'}
    return render(request,'core/index.html', context)
@login_required
def confirmacao_cadastro(request):
    return render(request,'core/confirmacao.html')

#CRUD_Aluno
@login_required
def lista_alunos(request):
    alunos = Aluno.objects.all()
    form = AlunoForm()
    data = {'alunos': alunos, 'form': form}
    return render(request, 'core/lista_aluno.html', data)
@login_required
def aluno_novo(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_confirmacao_cadastro')
    else:
        return render(request,'core/cadastro_alunos.html',{'form':form})
@login_required
def aluno_update(request, id):
    data={}
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(request.POST or None, instance=aluno)
    data['aluno']=aluno
    data['form']=form

    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_alunos')
    else:
        return render(request,'core/update_aluno.html',data)
@login_required
def aluno_delete(request, id):
    aluno = Aluno.objects.get(id=id)
    if request.method=='POST':
        aluno.delete()
        return redirect('core_lista_alunos')
    else:
        return render(request,'core/delete_confirm.html',{'obj':aluno})

#FIM CRUD_Aluno

#CRUD Professor
@login_required
def lista_professor(request):
    form = ProfessorForm()
    professor = Professor.objects.all()
    data = {'professor': professor, 'form': form}
    return render(request, 'core/lista_professor.html', data)
@login_required
def professor_novo(request):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_confirmacao_cadastro')
    else:
        return render(request,'core/cadastro_professor.html',{'form':form})
@login_required
def professor_update(request, id):
    data={}
    professor = Professor.objects.get(id=id)
    form = ProfessorForm(request.POST or None, instance=professor)
    data['professor']=professor
    data['form']=form

    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_professor')
    else:
        return render(request,'core/update_professor.html',data)
@login_required
def professor_delete(request, id):
    professor = Professor.objects.get(id=id)
    if request.method=='POST':
        professor.delete()
        return redirect('core_lista_professor')
    else:
        return render(request,'core/delete_confirm.html',{'obj':professor})
#FIM CRUD Professor


def lista_cursos(request):
    form = CursoForm()
    curso = Curso.objects.all()
    data = {'curso':curso, 'form': form}
    return render(request, 'core/lista_cursos.html', data)

def curso_novo(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return  redirect('core_confirmacao_cadastro')
    else:
        return render(request, 'core/cadastro_curso.html',{'form':form})
