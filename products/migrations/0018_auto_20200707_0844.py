# Generated by Django 3.0.8 on 2020-07-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20200707_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/media/defaults/default_product.jpg', null=True, upload_to='product'),
        ),
    ]
