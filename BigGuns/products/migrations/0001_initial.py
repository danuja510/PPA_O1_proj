# Generated by Django 3.0.5 on 2020-04-05 21:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('manufacturer', models.CharField(max_length=100)),
            ],
        ),
    ]
