# Generated by Django 4.1.2 on 2022-12-03 16:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestionpfe', '0015_cahierdecharge'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CahierdeCharge',
            new_name='CahierCharge',
        ),
    ]