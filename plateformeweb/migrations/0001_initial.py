# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-07 10:14
from __future__ import unicode_literals

import address.models
import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_prices.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('address', '0002_auto_20160213_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Abilities')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Activity type')),
                ('slug', autoslug.fields.AutoSlugField(default='', editable=False, populate_from='name')),
                ('description', models.TextField(default='', verbose_name='Activity description')),
                ('picture', models.ImageField(upload_to='activities/', verbose_name='Image')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Condition Type')),
                ('resume', models.CharField(default='', max_length=100, verbose_name='Condition resume')),
                ('description', models.TextField(default='', verbose_name='Condition description')),
                ('price', django_prices.models.MoneyField(blank=True, currency='EUR', decimal_places=2, default='5', max_digits=9, verbose_name='tarif')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=150, verbose_name='Title')),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('publish_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publication date and time')),
                ('slug', autoslug.fields.AutoSlugField(default='', editable=False, populate_from='title', unique=True)),
                ('starts_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start date and time')),
                ('ends_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='End date and time')),
                ('available_seats', models.IntegerField(blank=True, default=0, verbose_name='Available seats')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attendees', models.ManyToManyField(blank=True, related_name='attendee_user', to=settings.AUTH_USER_MODEL, verbose_name='Attendees')),
                ('condition', models.ManyToManyField(blank=True, related_name='condition_activity', to='plateformeweb.Condition', verbose_name='Conditions')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Organization name')),
                ('active', models.BooleanField(verbose_name='Active')),
                ('slug', autoslug.fields.AutoSlugField(default='', editable=False, populate_from='name', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.SmallIntegerField(choices=[(0, 'Visitor'), (10, 'Member'), (20, 'Volunteer'), (30, 'Admin')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(default='', verbose_name='Description')),
                ('type', models.CharField(choices=[('rc', 'Repair café'), ('sc', 'School')], default='ot', max_length=2, verbose_name='Type')),
                ('slug', autoslug.fields.AutoSlugField(default='', editable=False, populate_from='name', unique=True)),
                ('picture', models.ImageField(upload_to='places/', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', address.models.AddressField(default='', on_delete=django.db.models.deletion.CASCADE, to='address.Address', verbose_name='Postal address')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plateformeweb.Organization')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationVolunteer',
            fields=[
                ('organizationperson_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='plateformeweb.OrganizationPerson')),
                ('tagline', models.TextField(verbose_name='Tagline')),
                ('abilities', models.ManyToManyField(to='plateformeweb.Abilities')),
            ],
            bases=('plateformeweb.organizationperson',),
        ),
        migrations.AddField(
            model_name='organizationperson',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plateformeweb.Organization'),
        ),
        migrations.AddField(
            model_name='organizationperson',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='plateformeweb.Place'),
        ),
        migrations.AddField(
            model_name='event',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plateformeweb.Organization'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizers',
            field=models.ManyToManyField(blank=True, related_name='organizer_user', to=settings.AUTH_USER_MODEL, verbose_name='Organizers'),
        ),
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='presents',
            field=models.ManyToManyField(blank=True, related_name='present_user', to=settings.AUTH_USER_MODEL, verbose_name='Presents'),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='plateformeweb.Activity'),
        ),
        migrations.CreateModel(
            name='OrganizationAdministrator',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('plateformeweb.organizationperson',),
        ),
        migrations.CreateModel(
            name='OrganizationMember',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('plateformeweb.organizationperson',),
        ),
        migrations.CreateModel(
            name='OrganizationVisitor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('plateformeweb.organizationperson',),
        ),
        migrations.CreateModel(
            name='PublishedEvent',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('plateformeweb.event',),
        ),
        migrations.AlterUniqueTogether(
            name='organizationperson',
            unique_together=set([('organization', 'user', 'role')]),
        ),
    ]
