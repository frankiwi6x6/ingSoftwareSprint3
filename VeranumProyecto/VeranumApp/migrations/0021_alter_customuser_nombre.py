# Generated by Django 4.2.2 on 2023-06-21 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VeranumApp', '0020_alter_customuser_managers_alter_customuser_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='nombre',
            field=models.CharField(default='testName', max_length=80),
        ),
    ]
