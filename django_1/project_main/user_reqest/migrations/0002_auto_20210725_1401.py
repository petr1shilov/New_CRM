# Generated by Django 3.2.5 on 2021-07-25 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_reqest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_request',
            old_name='title_2',
            new_name='user_conact',
        ),
        migrations.RenameField(
            model_name='user_request',
            old_name='title_1',
            new_name='user_name',
        ),
    ]
