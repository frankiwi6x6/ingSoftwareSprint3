# Generated by Django 4.2.2 on 2023-06-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VeranumApp', '0016_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='contrasenna',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]