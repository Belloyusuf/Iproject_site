# Generated by Django 3.2.9 on 2022-01-18 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='username',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='email',
            field=models.CharField(max_length=250),
        ),
    ]
