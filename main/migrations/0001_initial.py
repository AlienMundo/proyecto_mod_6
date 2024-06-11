# Generated by Django 5.0.6 on 2024-06-07 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=15)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
