# Generated by Django 4.1 on 2022-08-12 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='technician',
            name='Id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
