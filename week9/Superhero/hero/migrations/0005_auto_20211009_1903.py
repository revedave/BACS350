# Generated by Django 3.2.6 on 2021-10-10 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0004_auto_20211001_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='strength',
            field=models.CharField(default='hero', max_length=200),
        ),
        migrations.AddField(
            model_name='superhero',
            name='weakness',
            field=models.CharField(default='hero', max_length=200),
        ),
    ]
