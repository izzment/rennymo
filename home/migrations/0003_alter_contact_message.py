# Generated by Django 4.1 on 2024-10-31 17:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_alter_contact_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="message",
            field=models.CharField(max_length=1000),
        ),
    ]
