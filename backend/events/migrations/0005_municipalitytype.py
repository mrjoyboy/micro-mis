# Generated by Django 5.1.4 on 2024-12-17 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_district_area_sq_km_alter_province_area_sq_km'),
    ]

    operations = [
        migrations.CreateModel(
            name='MunicipalityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_code', models.CharField(max_length=50)),
            ],
        ),
    ]
