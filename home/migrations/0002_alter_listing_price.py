# Generated by Django 3.2.7 on 2021-10-14 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Price',
            field=models.CharField(max_length=250, verbose_name='price'),
        ),
    ]