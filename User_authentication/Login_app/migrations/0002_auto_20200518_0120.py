# Generated by Django 3.0.3 on 2020-05-18 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='facebook_url',
            new_name='facebook_id',
        ),
    ]
