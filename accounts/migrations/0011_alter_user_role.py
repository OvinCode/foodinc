# Generated by Django 4.2.3 on 2023-08-01 21:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0010_alter_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.PositiveSmallIntegerField(
                blank=True, choices=[(1, "Restaurant"), (2, "Customer")], null=True
            ),
        ),
    ]
