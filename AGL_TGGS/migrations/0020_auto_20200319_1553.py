# Generated by Django 3.0.3 on 2020-03-19 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AGL_TGGS', '0019_auto_20200319_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='assignee',
            field=models.CharField(max_length=50, null=True),
        ),
    ]