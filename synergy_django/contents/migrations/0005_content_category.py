# Generated by Django 3.0.5 on 2021-01-17 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_content_footnote'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='category',
            field=models.ManyToManyField(to='contents.Category'),
        ),
    ]
