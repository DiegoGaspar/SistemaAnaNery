# Generated by Django 2.2.6 on 2019-10-02 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_aluno_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='user',
        ),
        migrations.AddField(
            model_name='aluno',
            name='endereco',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='nome',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='telefone',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
