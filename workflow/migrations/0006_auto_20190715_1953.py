# Generated by Django 2.2.3 on 2019-07-15 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0005_auto_20190715_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='action',
        ),
        migrations.RemoveField(
            model_name='task',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='task',
            name='service_type',
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='sequence',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='ProviderTask',
            fields=[
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='workflow.Task')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflow.Action')),
                ('provider_service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflow.ProviderServiceType')),
            ],
        ),
    ]
