# Generated by Django 4.0.4 on 2022-05-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_main', '0006_parts_n_accessories_model_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='parts_n_accessories_model',
            name='product_image',
            field=models.ImageField(default=None, upload_to='productImage/'),
            preserve_default=False,
        ),
    ]