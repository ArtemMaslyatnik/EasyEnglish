# Generated by Django 5.1.3 on 2024-12-18 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ee', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relatedword',
            name='relate_english_word',
        ),
    ]
