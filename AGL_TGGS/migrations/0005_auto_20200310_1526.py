# Generated by Django 3.0.3 on 2020-03-10 07:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AGL_TGGS', '0004_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='member',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
