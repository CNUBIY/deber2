from django.db import models

# Create your models here.
class Provincia(models.Model):
    id_cc=models.AutoField(primary_key=True)
    nombre_cc=models.CharField(max_length=150)
    codigo_cc=models.IntegerField()
    foto_cc=models.FileField(upload_to='banderas',null=True,blank=True)

    def __str__(self):
        fila="{0} - {1}"
        return fila.format(self.id_cc, self.nombre_cc)

class Tipo(models.Model):
    id_cc=models.AutoField(primary_key=True)
    nombre_cc=models.CharField(max_length=150)
    dificultad_cc=models.CharField(max_length=150)
    descripcion_cc=models.TextField()

    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.id_cc, self.nombre_cc)

class Ingrediente(models.Model):
    id_cc=models.AutoField(primary_key=True)
    nombre_cc=models.CharField(max_length=150)
    tipo_cc=models.CharField(max_length=150)
    foto_cc=models.FileField(upload_to='ingredientes',null=True,blank=True)

    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.id_cc, self.nombre_cc)



class Cliente(models.Model):
    id_cc=models.AutoField(primary_key=True)
    cedula_cc=models.CharField(max_length=10)
    nombre_cc=models.CharField(max_length=150)
    correo_cc=models.CharField(max_length=150)
    provincia_cc=models.ForeignKey(Provincia,null=True,blank=True, on_delete=models.PROTECT)

    def __str__(self):
        fila="{0}: {1} - {2}"
        return fila.format(self.cedula_cc, self.nombre_cc, self.correo_cc)


class Pedido(models.Model):
    id_cc=models.AutoField(primary_key=True)
    fecha_cc=models.DateTimeField()
    tipopago_cc=models.CharField(max_length=150)
    servicio_cc=models.CharField(max_length=150)
    cliente_cc=models.ForeignKey(Cliente,null=True,blank=True, on_delete=models.PROTECT)

    def __str__(self):
        fila="{0} - Pedido el: {1}"
        return fila.format(self.id_cc, self.fecha_cc)

class Platillo(models.Model):
    id_cc=models.AutoField(primary_key=True)
    nombre_cc=models.CharField(max_length=150)
    costou_cc=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    foto_cc=models.FileField(upload_to='platillos',null=True,blank=True)
    tipo_cc=models.ForeignKey(Tipo,null=True,blank=True, on_delete=models.PROTECT)

    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.id_cc, self.nombre_cc)


class Detalle(models.Model):
    id_cc=models.AutoField(primary_key=True)
    mesa_cc=models.PositiveIntegerField()
    costot_cc=models.DecimalField(max_digits=10, decimal_places=2)
    descripcion_cc=models.TextField(null=True, blank=True)
    platillo_cc=models.ManyToManyField(Platillo)
    pedido_cc=models.ForeignKey(Pedido,null=True,blank=True, on_delete=models.PROTECT)

    def __str__(self):
        fila="{0} de {1}"
        return fila.format(self.mesa_cc, self.costot_cc)



class Receta(models.Model):
    id_cc=models.AutoField(primary_key=True)
    tiempo_cc=models.CharField(max_length=150)
    origen_cc=models.CharField(max_length=150)
    indicaciones_cc=models.TextField()
    platillo_cc=models.ForeignKey(Platillo,null=True,blank=True, on_delete=models.PROTECT)
    ingrediente_cc=models.ManyToManyField(Ingrediente)

    def __str__(self):
        fila="{0} de {1}"
        return fila.format(self.tiempo_cc, self.platillo_cc)
