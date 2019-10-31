from django.db import models


#classe cadastro de aluno
class Aluno(models.Model):
    SEXO_CHOICES = ((u'M', 'Masculino'), (u'F', 'Feminino'))
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=1)
    cpf = models.CharField(max_length=20, blank=True)
    coren = models.CharField(max_length=20, blank=True)
    pai = models.CharField(max_length=20, blank=True)
    mae = models.CharField(max_length=20, blank=True)
    nascimento = models.DateField(blank=True)

    def __str__(self):
        return self.nome

#classe cadastro de professor
class Professor(models.Model):
    SEXO_CHOICES = ((u'M', 'Masculino'), (u'F', 'Feminino'))
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=1)
    cpf = models.CharField(max_length=20, blank=True)
    coren = models.CharField(max_length=20, blank=True)
    pai = models.CharField(max_length=20, blank=True)
    mae = models.CharField(max_length=20, blank=True)
    nascimento = models.DateField(blank=True)


    def __str__(self):
        return self.nome

#class de cadastro de curso--background: url(../img/about-bg.jpg);
class Curso(models.Model):
    codigo = models.IntegerField()
    nomeCurso = models.CharField(max_length=20)
    investimento = models.DecimalField(max_digits=6,decimal_places=2)
    desconto = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    manha= models.BooleanField(default=False)
    tarde = models.BooleanField(default=False)
    noite = models.BooleanField(default=False)
    outroHorario = models.BooleanField(default=False)
    facilitador = models.ManyToManyField(Professor)
    obs = models.TextField()

    def __str__(self):
        return self.nomeCurso

