from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Cadastro(models.Model):

    sexo = (
           ('0', 'Masculino'),
           ('1', 'Feminino'),
           ('2', 'Não Binário')
    )

    estado_civil =(
                  ('0', 'Solteiro(a)'),
                  ('1', 'Casado(a)'),
                  ('2', 'Viúvo(a)'),
                  ('3', 'Divorciado(a)')
    )

    nome = models.CharField(max_length=200)
    idade = models.CharField(max_length=20)
    nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1, choices=sexo)
    estado_civil =models.CharField(max_length=1, choices=estado_civil)

    def __str__(self):
        return self.nome
