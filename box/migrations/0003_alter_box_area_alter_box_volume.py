# Generated by Django 5.0 on 2023-12-15 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0002_alter_box_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='area',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='box',
            name='volume',
            field=models.FloatField(null=True),
        ),
    ]
