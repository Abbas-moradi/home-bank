# Generated by Django 4.2.7 on 2023-11-27 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_remove_branchsetting_percent_branchsetting_wage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(choices=[('LA', 'Loan application'), ('AO', 'Account opening'), ('R', 'Review'), ('P', 'Proposal')], max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('seen', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
