# Generated by Django 4.2.7 on 2023-11-10 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(null=True, upload_to='media/%Y/%m/%d/'),
        ),
    ]