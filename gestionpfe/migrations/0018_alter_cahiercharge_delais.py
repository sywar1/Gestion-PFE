# Generated by Django 4.1.2 on 2022-12-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpfe', '0017_rename_nom_cahiercharge_nomprojet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cahiercharge',
            name='delais',
            field=models.DateField(),
        ),
    ]