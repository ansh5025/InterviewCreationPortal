# Generated by Django 3.2.9 on 2021-11-26 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='scheduled_slots',
            field=models.ManyToManyField(null=True, to='task.Slot'),
        ),
        migrations.AlterField(
            model_name='interviewer',
            name='scheduled_slots',
            field=models.ManyToManyField(null=True, to='task.Slot'),
        ),
    ]
