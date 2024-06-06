from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Instalacion(models.Model):
    TIPO_FIBRA_CHOICES = [
        ('400mb', '400mb'),
        ('800mb', '800mb'),
        ('1gb', '1GB'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_fibra = models.CharField(max_length=10, choices=TIPO_FIBRA_CHOICES)
    router_bicanal = models.BooleanField(default=False)
    extensor_wifi = models.BooleanField(default=False)
    fecha_instalacion = models.DateField()
    hora_instalacion = models.TimeField()
    comentario_adicional = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'Instalacion {self.tipo_fibra} para {self.cliente}'
