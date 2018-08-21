# Generated by Django 2.0.5 on 2018-08-18 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtask',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='subtask',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='subtask',
            name='reporter',
        ),
        migrations.RemoveField(
            model_name='subtask',
            name='task_status',
        ),
        migrations.AddField(
            model_name='task',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtask', to='tasks.Task', to_field='ref_id'),
        ),
        migrations.DeleteModel(
            name='SubTask',
        ),
    ]
