# Generated by Django 3.0.7 on 2020-08-10 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20200806_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='download_time',
            name='card_pk',
            field=models.IntegerField(default=False),
        ),
    ]
