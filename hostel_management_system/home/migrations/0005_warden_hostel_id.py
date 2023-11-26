# Generated by Django 4.1.3 on 2023-01-21 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_warden"),
    ]

    operations = [
        migrations.AddField(
            model_name="warden",
            name="hostel_id",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="home.hostels",
            ),
            preserve_default=False,
        ),
    ]
