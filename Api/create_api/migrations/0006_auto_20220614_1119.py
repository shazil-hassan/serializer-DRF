# Generated by Django 2.2.10 on 2022-06-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_api', '0005_auto_20220614_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(max_length=3),
        ),
    ]
