# Generated by Django 4.1.7 on 2023-03-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo2app', '0002_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='img',
            field=models.ImageField(upload_to='new'),
        ),
    ]
