# Generated by Django 4.1.3 on 2022-11-12 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_tag_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
