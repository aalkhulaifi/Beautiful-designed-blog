# Generated by Django 2.1 on 2018-09-21 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article_sub_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_currentuser',
            field=models.BooleanField(default=False),
        ),
    ]
