# Generated by Django 3.0.3 on 2020-03-10 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AGL_TGGS', '0002_remove_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]