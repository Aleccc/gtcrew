# Generated by Django 3.2.5 on 2021-07-24 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0018_auto_20200819_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='regatta',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='result',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
