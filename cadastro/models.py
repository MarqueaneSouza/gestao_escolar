from django.db import models


class Escola(models.Model):
    nome = models.CharField(max_length=225)
    endereco = models.TextField()

    def __str__(self):
        return self.nome
    
class Profissional(models.Model):
    CARGOS = [
        ('Professor', 'Professor'),
        ('Diretor', 'Diretor'),
        ('Gestor de Serviços Educacionais', 'Gestor de Serviços Educacionais'),
        ('Coordenador', 'Coordenador'),
        ('Secretário Escolar', 'Secretário Escolar'),
        ('Escriturário', 'Escriturário'),
        ('Assistente de Educação', 'Assistente de Educação'),
        ('Auxiliar de Serviços', 'Auxiliar de Serviços'),
        ('Outro', 'Outro'),
    ]

    nome = models.CharField(max_length=255)
    cargo = models.CharField(max_length=50, choices=CARGOS)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.cargo}"