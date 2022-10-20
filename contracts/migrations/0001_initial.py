# Generated by Django 4.1.2 on 2022-10-20 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False, verbose_name='Contract Signed')),
                ('amount', models.FloatField()),
                ('payment_due', models.DateTimeField(verbose_name='payment due')),
                ('client', models.ForeignKey(limit_choices_to={'status': 'SUCCESS'}, on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('sales_contact', models.ForeignKey(limit_choices_to={'user_type': 'USER_SALES'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='sales contact')),
            ],
        ),
    ]