# Generated by Django 3.2.7 on 2022-04-23 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20220422_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='movies.Actor'),
        ),
    ]