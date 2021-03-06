# Generated by Django 2.2.3 on 2019-07-16 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0006_auto_20190715_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminTask',
            fields=[
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='workflow.Task')),
                ('name', models.CharField(max_length=200)),
                ('instructions', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='TaskList',
            new_name='TaskSequence',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='action',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='provider_service_type',
        ),
        migrations.RemoveField(
            model_name='task',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='task',
            name='name',
        ),
        migrations.AddField(
            model_name='providertask',
            name='instructions',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ProviderTaskOption',
            fields=[
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='workflow.Task')),
                ('provider_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflow.ProviderTask')),
            ],
        ),
    ]
