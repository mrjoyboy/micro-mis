# Generated by Django 5.1.4 on 2024-12-23 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_alter_projectfile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='disability',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]
