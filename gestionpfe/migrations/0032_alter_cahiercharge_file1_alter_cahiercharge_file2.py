# Generated by Django 4.1.2 on 2022-12-04 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpfe', '0031_alter_cahiercharge_file1_alter_cahiercharge_file2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cahiercharge',
            name='file1',
            field=models.FileField(upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='cahiercharge',
            name='file2',
            field=models.FileField(upload_to='photos'),
        ),
    ]
