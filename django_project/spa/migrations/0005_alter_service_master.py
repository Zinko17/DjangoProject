# Generated by Django 3.2.3 on 2021-05-28 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0004_alter_service_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='spa.master'),
        ),
    ]
