# Generated by Django 2.2.5 on 2020-02-04 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_user_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fist_name',
            new_name='first_name',
        ),
    ]