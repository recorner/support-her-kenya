# Generated by Django 2.2.3 on 2019-08-23 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0022_auto_20190822_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='fee',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Fee'),
        ),
    ]