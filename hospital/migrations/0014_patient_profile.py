# Generated by Django 4.2.6 on 2023-11-20 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0013_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.TextField()),
                ('daignosis', models.TextField()),
                ('age', models.PositiveSmallIntegerField(default=None)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=None, max_length=10)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.appointment')),
            ],
        ),
    ]