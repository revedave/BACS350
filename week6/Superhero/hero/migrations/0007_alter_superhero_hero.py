# Generated by Django 3.2.6 on 2021-10-11 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0006_auto_20211009_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='hero',
            field=models.CharField(max_length=200),
        ),
    ]