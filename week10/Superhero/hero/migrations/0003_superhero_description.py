# Generated by Django 3.2.6 on 2021-10-01 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_auto_20210928_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='description',
            field=models.CharField(default='0000', editable=False, max_length=500),
        ),
    ]
