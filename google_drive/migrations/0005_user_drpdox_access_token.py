# Generated by Django 2.2.5 on 2019-09-19 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_drive', '0004_auto_20190913_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='drpdox_access_token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
