from django.db import models

# Create your models here.
class Contato(models.Model):

    estado_civis = [
        ('S', 'Solteiro'),
        ('C','Casado'),
        ('D','Divorciado'),
        ('V','Viúvo')
    ]

    nome = models.CharField(max_length=200)
    apelido = models.CharField(max_length=30)    
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=10, verbose_name='Número')
    complemento = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)
    estado_civil = models.CharField(max_length=1, choices=estado_civis, null=True)

    def __str__(self):
        return self.nome
       
    
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
