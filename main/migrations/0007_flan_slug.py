# Generated by Django 5.0.6 on 2024-06-17 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_cliente_customer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]