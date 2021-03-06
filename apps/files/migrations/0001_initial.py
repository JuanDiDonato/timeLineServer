# Generated by Django 4.0.1 on 2022-01-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_file', models.DateField(auto_now_add=True)),
                ('file', models.FileField(null=True, upload_to='files')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
            },
        ),
    ]
