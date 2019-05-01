from django.db import models

class Barbero(models.Model):
    codbarbero = models.AutoField(primary_key=True)
    barberonom = models.CharField(max_length=150,blank=False,null=False)
    fecharegistro = models.DateField()
    descripcion = models.TextField()
    correo = models.EmailField(max_length=250)

    class Meta:
        verbose_name= 'Barbero'
        verbose_name_plural='Barberos'
        ordering=['barberonom']

    def __str__(self):
        return self.barberonom

class Cliente(models.Model):
    codcliente =models.AutoField('Codigo',primary_key=True)
    clientenom =models.CharField('Cliente',max_length=150,blank=False,null=False)
    fecharegistro =models.DateField()
    telefono = models.CharField('Telefono',max_length=12)
    correo=models.EmailField('Correo',max_length=250)

    class Meta:
        verbose_name= 'Cliente'
        verbose_name_plural='Clientes'
        ordering=['clientenom']

    def __str__(self):
        return self.clientenom       

class Servicio(models.Model):
    codserv =models.AutoField('Codigo',primary_key=True)
    servicio =models.CharField('Servicio',max_length=150,blank=False,null=False)
    nomcorto =models.CharField('Abreviatura',max_length=50,blank=False,null=False)
    fecharegistro =models.DateField()

    class Meta:
        verbose_name= 'Servicio'
        verbose_name_plural='Servicios'
        ordering=['nomcorto']

    def __str__(self):
        return self.servicio

class Reserva(models.Model):
    codreserva =models.AutoField(primary_key=True)
    codbarbero = models.ForeignKey(Barbero,on_delete=models.CASCADE)
    codclie = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    codserv = models.ManyToManyField(Servicio)
    fecha = models.DateField()
    obs = models.TextField()

    class Meta:
        verbose_name= 'Reserva'
        verbose_name_plural='Reservas'
        ordering=['fecha']
    


# Create your models here.y = 
