# Generated by Django 3.0.2 on 2020-01-30 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campanhas', '0003_campanha_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campanha',
            name='pub_date',
            field=models.DateField(default='2020-01-01', verbose_name='date published'),
        ),
    ]
