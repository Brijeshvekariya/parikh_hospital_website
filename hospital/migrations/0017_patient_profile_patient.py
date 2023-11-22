# Generated by Django 4.2.6 on 2023-11-22 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0016_alter_patient_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_profile',
            name='patient',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.appointment'),
        ),
    ]
