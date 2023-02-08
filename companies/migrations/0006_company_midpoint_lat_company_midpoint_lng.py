# Generated by Django 4.1.6 on 2023-02-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_company_test_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='midpoint_lat',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='midpoint_lng',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]
