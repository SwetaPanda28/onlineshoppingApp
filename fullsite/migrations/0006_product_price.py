# Generated by Django 3.2.4 on 2021-08-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullsite', '0005_alter_product_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, max_length=99999999),
            preserve_default=False,
        ),
    ]
