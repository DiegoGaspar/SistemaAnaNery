# Generated by Django 2.2.6 on 2019-10-24 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='curso',
        ),
    ]
