# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-08 12:07
from __future__ import unicode_literals

import autoslug.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('gender', models.CharField(choices=[('', '----'), ('m', 'Male'), ('f', 'Female')], default='m', max_length=1, verbose_name='Gender')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('image', models.FileField(blank=True, null=True, upload_to='photos')),
                ('contact', models.CharField(blank=True, max_length=20, null=True, verbose_name='Contact')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified At')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, default=None, editable=False, populate_from='first_name', unique=True)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('code', models.CharField(max_length=10, null=True, verbose_name='Code')),
                ('acronym', models.CharField(max_length=10, null=True, verbose_name='Acronym')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('type', models.CharField(choices=[('', '----'), ('ac', 'Academic'), ('ad', 'Administrative')], max_length=2, verbose_name='Type')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified At')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, default=None, editable=False, populate_from='acronym', unique_with=('id',))),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='duet_admin.Department', verbose_name='Department'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
