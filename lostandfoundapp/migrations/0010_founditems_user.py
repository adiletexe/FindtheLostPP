# Generated by Django 4.0.5 on 2022-08-17 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lostandfoundapp', '0009_founditems_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='founditems',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
