# Generated by Django 3.1.7 on 2021-05-25 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='mobile_no',
            field=models.CharField(max_length=12),
        ),
    ]
