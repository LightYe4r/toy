# Generated by Django 4.2.2 on 2023-07-12 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catchtable', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]