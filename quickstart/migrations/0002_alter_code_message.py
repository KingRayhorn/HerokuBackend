# Generated by Django 4.0.6 on 2022-10-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='message',
            field=models.TextField(),
        ),
    ]
