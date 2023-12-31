# Generated by Django 4.2.7 on 2023-11-06 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bankaccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True)),
                ('loan_amount', models.IntegerField()),
                ('end_date', models.DateField(null=True)),
                ('wag_amount', models.IntegerField()),
                ('term', models.IntegerField()),
                ('installment_number', models.PositiveSmallIntegerField()),
                ('delay_days', models.PositiveSmallIntegerField(default=0)),
                ('installment_paid', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('clearing', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankaccount.account')),
            ],
            options={
                'verbose_name': 'Loan',
                'verbose_name_plural': 'Loans',
                'ordering': ('start_date',),
            },
        ),
        migrations.CreateModel(
            name='LoanTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_installment', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('loan_balance', models.IntegerField()),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.loan')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankaccount.transaction')),
            ],
            options={
                'verbose_name': 'LoanTransaction',
                'verbose_name_plural': 'LoanTransactions',
                'ordering': ('date',),
            },
        ),
    ]
