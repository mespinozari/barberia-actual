# Generated by Django 2.2 on 2019-04-09 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservaBarberia', '0004_reserva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='codserv',
        ),
        migrations.AddField(
            model_name='reserva',
            name='codserv',
            field=models.ManyToManyField(to='ReservaBarberia.Servicio'),
        ),
    ]
