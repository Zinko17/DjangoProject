# Generated by Django 3.2.3 on 2021-05-28 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0006_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='master',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spa.master'),
            preserve_default=False,
        ),
    ]
