# Generated by Django 4.1 on 2024-11-01 06:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_alter_contact_phone"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Contact",
            new_name="Message",
        ),
    ]
