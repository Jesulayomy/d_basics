# Generated by Django 5.0.1 on 2024-01-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_todolist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='is_daily',
            field=models.BooleanField(default=False),
        ),
    ]