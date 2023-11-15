from distutils.command.upload import upload
from django.db import models

class Produto(models.Model):
    nome=models.CharField(max_length=100)
    image=models.ImageField(upload_to="prod_imgs/")
    preco=models.PositiveIntegerField()

    def __str__(self):
        return self.nome