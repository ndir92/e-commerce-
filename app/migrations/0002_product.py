# Generated by Django 4.0.1 on 2022-01-19 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ecommerce/pimg')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]