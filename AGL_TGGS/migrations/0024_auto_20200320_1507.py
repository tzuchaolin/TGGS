# Generated by Django 3.0.3 on 2020-03-20 07:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AGL_TGGS', '0023_assignee_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignee',
            name='name',
        ),
        migrations.AddField(
            model_name='job',
            name='gid',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='gid',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='JobDivision',
        ),
    ]