# Generated by Django 4.2.6 on 2024-08-13 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ee', '0022_serv_transcription_eng_serv_transcription_use'),
    ]

    operations = [
        migrations.AddField(
            model_name='serv',
            name='sound_path',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
