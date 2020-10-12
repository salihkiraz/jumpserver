# Generated by Django 2.2.13 on 2020-10-12 05:53

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('namespaces', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('type', models.CharField(choices=[('string', 'String'), ('integer', 'Integer'), ('list', 'List'), ('ip', 'IP')], default='string', max_length=32, verbose_name='Type')),
                ('default', jsonfield.fields.JSONField(default=dict)),
                ('choices', jsonfield.fields.JSONField(default=dict)),
                ('required', models.BooleanField(default=False, verbose_name='Required')),
            ],
            options={
                'verbose_name': 'Prop Field',
            },
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('category', models.CharField(choices=[('os', 'Operation System'), ('network_device', 'Network Device'), ('app', 'Application'), ('cloud', 'Cloud'), ('other', 'Other')], default='os', max_length=64, verbose_name='Category')),
                ('protocol', models.CharField(max_length=32, verbose_name='Protocol')),
                ('base_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sub_types', to='accounts.AccountType', verbose_name='Base Type')),
                ('prop_fields', models.ManyToManyField(to='accounts.PropField', verbose_name='Properties Definition')),
            ],
            options={
                'verbose_name': 'Account Type',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('username', models.CharField(blank=True, max_length=256, null=True, verbose_name='Username')),
                ('address', models.CharField(max_length=1024, verbose_name='Address')),
                ('secret_type', models.CharField(choices=[('password', 'Password'), ('ssh-key', 'SSH Key'), ('token', 'Token'), ('cert', 'Cert')], max_length=32, verbose_name='Secret type')),
                ('secret', models.TextField(verbose_name='Secret')),
                ('extra_props', jsonfield.fields.JSONField(default=dict)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('comment', models.TextField(default='', verbose_name='Comment')),
                ('namespace', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='namespaces.Namespace', verbose_name='Namespace')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.AccountType', verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Account',
                'permissions': (('gain_secret', 'Can gain secret'), ('connect_account', 'Can connect account')),
            },
        ),
    ]