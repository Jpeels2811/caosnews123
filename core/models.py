from django.db import models

# Create your models here.
class Categoria(models.Model):
  idCategoria = models.IntegerField(primary_key = True, verbose_name = 'Id de categoria')
  nombreCategoria = models.CharField(max_length = 20, verbose_name = 'Nombre de la categoria')

  def __str__(self):
    return self.nombreCategoria

class Noticia(models.Model):
  codigo = models.CharField(max_length = 5, primary_key = True, verbose_name = 'N° registro')
  titulo = models.CharField(max_length = 50, verbose_name = 'Titulo Noticia')
  fecha = models.CharField (max_length = 10, verbose_name = 'Fecha')
  ubicacion = models.CharField(max_length= 50, verbose_name='Ubicacion')
  descripcion = models.CharField(max_length= 2000, verbose_name='Cuerpo de la noticia' ) 
  categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)

  def __str__(self):
    return self.codigo