# Generated by Django 3.0.3 on 2020-03-13 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AGL_TGGS', '0005_auto_20200312_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='amount',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]