# Generated by Django 3.2.9 on 2022-01-21 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_project_old_price'),
        ('content', '0002_auto_20220121_0255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('company', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=150, verbose_name='Course Name')),
                ('topic', models.CharField(max_length=50, verbose_name='Project Topic')),
                ('description', models.TextField(verbose_name='Project Description')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Username')),
                ('email', models.EmailField(max_length=250, verbose_name='Your Email')),
                ('body', models.TextField(verbose_name='Your comment')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='projectapp.project')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
