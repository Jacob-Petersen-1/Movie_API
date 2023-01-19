# Generated by Django 4.1.5 on 2023-01-19 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('description', models.CharField(max_length=255)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
