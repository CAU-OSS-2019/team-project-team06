# Generated by Django 2.1.7 on 2019-06-01 11:58

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='file',
            field=models.FileField(null=True, upload_to='', validators=[mainapp.models.validate_file_extension]),
        ),
    ]
