# Generated by Django 4.0.8 on 2023-01-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default='products/images/img1.png', help_text='uplaod a product image', upload_to='products/images/', verbose_name='Image'),
        ),
    ]
