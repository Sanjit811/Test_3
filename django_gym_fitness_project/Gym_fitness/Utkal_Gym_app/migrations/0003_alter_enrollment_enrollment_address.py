# Generated by Django 5.0.4 on 2024-05-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Utkal_Gym_app', '0002_enrollment_membership_trainer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='Enrollment_Address',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
