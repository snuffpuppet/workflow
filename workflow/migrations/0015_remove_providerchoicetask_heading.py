# Generated by Django 2.2.3 on 2019-07-16 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0014_providerchoicetask_heading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='providerchoicetask',
            name='heading',
        ),
    ]
