# Generated by Django 3.2.2 on 2023-03-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0032_remove_fee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='payment',
            field=models.CharField(blank=True, choices=[('1', 'Espèces'), ('2', 'Online'), ('3', 'Chèque'), ('4', 'CB'), ('5', 'Monnaie Locale')], default='1', max_length=1),
        ),
    ]
