# Generated by Django 2.0.2 on 2018-03-13 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0006_auto_20180227_2003'),
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_answers',
        ),
        migrations.AddField(
            model_name='question',
            name='question_discipline',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='control_panel.Discipline', verbose_name='Предмет'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='question_title',
            field=models.TextField(verbose_name='Питання'),
        ),
    ]