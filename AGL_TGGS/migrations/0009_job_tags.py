# Generated by Django 3.0.3 on 2020-03-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AGL_TGGS', '0008_auto_20200318_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='tags',
            field=models.CharField(max_length=50, null=True),
        ),
    ]