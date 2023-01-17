# Generated by Django 4.0.8 on 2023-01-17 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=150, verbose_name='Full Name')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone Number')),
                ('town_city', models.CharField(max_length=150, verbose_name='Town/City/State')),
                ('postcode', models.CharField(max_length=50, verbose_name='Postcode')),
                ('address_line', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Line 1')),
                ('delivery_instructions', models.CharField(max_length=255, verbose_name='Delivery Instructions')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('default', models.BooleanField(default=False, verbose_name='Default')),
                ('custom_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
