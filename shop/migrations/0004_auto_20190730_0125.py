# Generated by Django 2.1.7 on 2019-07-29 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190730_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]