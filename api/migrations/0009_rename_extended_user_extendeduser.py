# Generated by Django 4.1.7 on 2023-03-16 04:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_rename_extendend_user_extended_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Extended_User',
            new_name='ExtendedUser',
        ),
    ]