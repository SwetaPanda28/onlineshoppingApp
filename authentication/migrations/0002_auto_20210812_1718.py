# Generated by Django 3.2.6 on 2021-08-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('emailAddress', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='signin',
        ),
    ]
