# Generated by Django 3.2.3 on 2021-05-25 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tenant", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={},
        ),
        migrations.AlterModelTable(
            name="user",
            table="user",
        ),
    ]
