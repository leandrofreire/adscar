# Generated by Django 3.0.2 on 2020-01-30 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campanhas', '0002_auto_20200129_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='campanha',
            name='pub_date',
            field=models.DateTimeField(default='01/01/2020', verbose_name='date published'),
        ),
    ]
