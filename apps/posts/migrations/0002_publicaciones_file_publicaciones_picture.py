# Generated by Django 4.0.1 on 2022-02-03 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0002_initial'),
        ('files', '0002_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='file',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='files.files'),
        ),
        migrations.AddField(
            model_name='posts',
            name='picture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camera.camera'),
        ),
    ]
