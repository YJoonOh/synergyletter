# Generated by Django 3.1.5 on 2021-01-21 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0006_auto_20210122_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
