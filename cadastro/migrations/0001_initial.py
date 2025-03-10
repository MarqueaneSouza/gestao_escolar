# Generated by Django 5.1.7 on 2025-03-08 23:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=225)),
                ('endereco', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cargo', models.CharField(choices=[('Professor', 'Professor'), ('Diretor', 'Diretor'), ('Gestor de Serviços Educacionais', 'Gestor de Serviços Educacionais'), ('Coordenador', 'Coordenador'), ('Secretário Escolar', 'Secretário Escolar'), ('Escriturário', 'Escriturário'), ('Assistente de Educação', 'Assistente de Educação'), ('Auxiliar de Serviços', 'Auxiliar de Serviços'), ('Outro', 'Outro')], max_length=50)),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.escola')),
            ],
        ),
    ]
