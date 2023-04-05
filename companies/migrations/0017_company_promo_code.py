# Generated by Django 4.2 on 2023-04-05 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0012_promocode'),
        ('companies', '0016_alter_company_billing_disabled_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='promo_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.promocode'),
        ),
    ]
