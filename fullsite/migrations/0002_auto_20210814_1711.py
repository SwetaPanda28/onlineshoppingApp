# Generated by Django 3.2.4 on 2021-08-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_desc', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='pruduct',
        ),
    ]
