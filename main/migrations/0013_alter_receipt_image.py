# Generated by Django 5.0.3 on 2025-01-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_receipt_author_alter_receipt_cooking_steps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='reciepts/image_from_client', verbose_name='Изображение'),
        ),
    ]
