# Generated by Django 4.0.5 on 2022-08-15 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostandfoundapp', '0004_alter_founditems_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founditems',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]