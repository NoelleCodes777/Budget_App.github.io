# Generated by Django 4.2.1 on 2023-05-17 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budgety', '0006_budget_alter_profile_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]