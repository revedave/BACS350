# Generated by Django 3.2.6 on 2021-10-01 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_superhero_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='hero',
            field=models.CharField(default='00000', max_length=200),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
