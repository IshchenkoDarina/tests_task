# Generated by Django 3.1 on 2020-08-25 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_auto_20200825_2200"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="amount_of_upvotes",
            field=models.IntegerField(default=0),
        ),
    ]
