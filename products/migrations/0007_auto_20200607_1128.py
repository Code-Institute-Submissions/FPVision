# Generated by Django 3.0.7 on 2020-06-07 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200607_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, default='7363463321', max_length=10, unique=True),
        ),
    ]
