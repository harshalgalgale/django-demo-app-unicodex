# Generated by Django 3.1 on 2020-09-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unicodex', '0003_codepoint_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codepoint',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
