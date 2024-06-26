# Generated by Django 3.2.3 on 2021-06-02 15:02

from django.db import migrations, models
import weirdlywired.helpers.secrets_helper


class Migration(migrations.Migration):

    dependencies = [
        ("tenant", "0002_auto_20210525_1551"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="key",
            field=models.CharField(
                default=weirdlywired.helpers.secrets_helper.get_random_key,
                max_length=32,
                unique=True,
            ),
        ),
    ]
