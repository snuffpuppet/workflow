# Generated by Django 2.2.3 on 2019-07-14 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0002_auto_20190714_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='task',
            name='service_type',
        ),
        migrations.AddField(
            model_name='task',
            name='provider_service_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.ProviderServiceType'),
        ),
    ]
