# Generated by Django 3.2.7 on 2021-10-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20211005_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]