# Generated by Django 4.2 on 2023-04-03 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('publish_date', models.DateField()),
                ('cover_art', models.URLField()),
            ],
        ),
    ]
