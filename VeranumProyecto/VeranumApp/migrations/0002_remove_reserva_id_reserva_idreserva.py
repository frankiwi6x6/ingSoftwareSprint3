# Generated by Django 4.2.2 on 2023-06-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VeranumApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='id',
        ),
        migrations.AddField(
            model_name='reserva',
            name='idReserva',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
