# Generated by Django 3.2.9 on 2022-01-21 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_remove_purchase_upload_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='upload_image',
            field=models.FileField(default=0, upload_to='purchase'),
            preserve_default=False,
        ),
    ]