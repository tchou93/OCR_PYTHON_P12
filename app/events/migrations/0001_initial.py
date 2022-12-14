# Generated by Django 4.1.2 on 2022-11-12 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(blank=True, max_length=100, verbose_name='event_name')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('event_status', models.BooleanField(default=False, verbose_name='Closed')),
                ('attendees', models.IntegerField(blank=True, null=True)),
                ('event_date', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('contract', models.OneToOneField(limit_choices_to={'status': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='contracts.contract')),
            ],
        ),
    ]
