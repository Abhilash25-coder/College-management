# Generated by Django 3.1.7 on 2021-04-29 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20210429_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.FileField(upload_to='pics'),
        ),
    ]