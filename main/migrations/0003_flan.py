# Generated by Django 5.0.6 on 2024-06-11 00:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_email_cliente_customer_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('nombre', models.CharField(max_length=64)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('imagen_url', models.URLField()),
                ('is_private', models.BooleanField(default=False)),
            ],
        ),
    ]