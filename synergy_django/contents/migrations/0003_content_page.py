# Generated by Django 3.0.5 on 2021-01-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='page',
            field=models.CharField(default='p.', max_length=10),
        ),
    ]
