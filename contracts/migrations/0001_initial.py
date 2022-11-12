# Generated by Django 4.1.2 on 2022-11-12 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('payment_due', models.DateField(verbose_name='payment due')),
                ('client', models.ForeignKey(limit_choices_to={'status': 'SUCCESS'}, on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
        ),
    ]
