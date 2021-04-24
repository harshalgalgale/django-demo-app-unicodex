# Generated by Django 3.1.7 on 2021-04-05 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='created_by',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='audit_trail_created', to='accounts.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='skills',
            name='updated_by',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='audit_trail_updated', to='accounts.user'),
            preserve_default=False,
        ),
    ]