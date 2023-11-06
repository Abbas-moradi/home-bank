# Generated by Django 4.2.7 on 2023-11-06 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.PositiveIntegerField()),
                ('balance', models.IntegerField()),
                ('opening_date', models.DateField(auto_now_add=True)),
                ('loan_status', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('closed', models.BooleanField(default=False)),
                ('closed_date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'ordering': ('account_number',),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('receipt', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('record', models.BooleanField(default=False)),
                ('record_date', models.DateField(null=True)),
                ('on_delete', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'ordering': ('registration_date',),
            },
        ),
        migrations.CreateModel(
            name='AccountTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_amount', models.IntegerField()),
                ('account_balance', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('on_delete', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankaccount.account')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankaccount.transaction')),
            ],
            options={
                'verbose_name': 'AccountTransaction',
                'verbose_name_plural': 'AccountTransactions',
                'ordering': ('date',),
            },
        ),
    ]