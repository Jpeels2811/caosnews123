from django.db import models

# Create your models here.
class Categoria(models.Model):
  idCategoria = models.IntegerField(primary_key = True, verbose_name = 'Id de categoria')
  nombreCategoria = models.CharField(max_length = 20, verbose_name = 'Nombre de la categoria')

  def str(self):
    return self.nombreCategoria

class Noticia(models.Model):
  codigo = models.CharField(max_length = 5, primary_key = True, verbose_name = 'Codigo')
  nombre = models.CharField(max_length = 20, verbose_name = 'Nombre noticia')
  fecha = models.CharField (max_length = 10, verbose_name = 'Fecha')
  categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)

  def str(self):
    return self.codigo