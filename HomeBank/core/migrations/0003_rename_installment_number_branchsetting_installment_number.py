# Generated by Django 4.2.7 on 2023-11-11 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_branchsetting_loan_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branchsetting',
            old_name='Installment_number',
            new_name='installment_number',
        ),
    ]