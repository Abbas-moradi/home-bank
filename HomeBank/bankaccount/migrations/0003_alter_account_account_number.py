# Generated by Django 4.2.7 on 2023-11-10 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccount', '0002_alter_account_account_number_alter_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.PositiveSmallIntegerField(editable=False, null=True, unique=True),
        ),
    ]
