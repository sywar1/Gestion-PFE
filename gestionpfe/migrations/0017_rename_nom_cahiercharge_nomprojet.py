# Generated by Django 4.1.2 on 2022-12-03 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpfe', '0016_rename_cahierdecharge_cahiercharge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cahiercharge',
            old_name='nom',
            new_name='nomprojet',
        ),
    ]
