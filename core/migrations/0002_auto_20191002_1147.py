# Generated by Django 2.2.6 on 2019-10-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='coren',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='aluno',
            name='mae',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='aluno',
            name='pai',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
