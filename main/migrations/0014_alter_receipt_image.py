# Generated by Django 5.0.3 on 2025-01-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_receipt_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image_from_client', verbose_name='Изображение'),
        ),
    ]
