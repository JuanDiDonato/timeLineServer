# Generated by Django 4.0.1 on 2022-01-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_picture', models.DateField(auto_now_add=True, null=None)),
                ('picture', models.ImageField(upload_to='pictures')),
            ],
            options={
                'verbose_name': 'Picture',
                'verbose_name_plural': 'Pictures',
            },
        ),
    ]
