# Generated by Django 4.2 on 2023-04-11 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_pet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='short_bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
