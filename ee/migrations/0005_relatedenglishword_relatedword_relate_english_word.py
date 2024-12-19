# Generated by Django 5.1.3 on 2024-12-19 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ee', '0004_delete_relatedenglishword'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedEnglishWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='relatedword',
            name='relate_english_word',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ee.relatedenglishword'),
            preserve_default=False,
        ),
    ]
