# Generated by Django 3.2 on 2024-08-01 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cats', to='cats.owner'),
            preserve_default=False,
        ),
    ]
