# Generated by Django 3.2.4 on 2021-08-24 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210813_1537'),
        ('fullsite', '0008_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_Add', models.ManyToManyField(to='fullsite.Address')),
                ('usr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
    ]