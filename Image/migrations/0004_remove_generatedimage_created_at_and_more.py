# Generated by Django 5.0.7 on 2024-11-06 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Image', '0003_generatedimage_likes_generatedimage_visibility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generatedimage',
            name='created_at',
        ),
        migrations.AddField(
            model_name='generatedimage',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
