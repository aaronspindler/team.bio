# Generated by Django 4.1.7 on 2023-03-26 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_pettype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pettype',
            options={'ordering': ['name']},
        ),
    ]
