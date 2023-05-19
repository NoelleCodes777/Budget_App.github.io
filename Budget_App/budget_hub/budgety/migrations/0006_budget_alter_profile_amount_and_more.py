# Generated by Django 4.2.1 on 2023-05-17 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgety', '0005_profile_bvn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('is_income', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='amount',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
