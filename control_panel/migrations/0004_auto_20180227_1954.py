# Generated by Django 2.0.2 on 2018-02-27 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0003_auto_20180227_1952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Кафедра', 'verbose_name_plural': 'Кафедри'},
        ),
        migrations.AlterModelOptions(
            name='discipline',
            options={'verbose_name': 'Предмет', 'verbose_name_plural': 'Предмети'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенти'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Викладач', 'verbose_name_plural': 'Викладачі'},
        ),
        migrations.AlterModelOptions(
            name='teacherrank',
            options={'verbose_name': 'Звання викладача', 'verbose_name_plural': 'Звання викладачів'},
        ),
        migrations.AlterModelOptions(
            name='troop',
            options={'verbose_name': 'Взвод', 'verbose_name_plural': 'Взводи'},
        ),
    ]
