# Generated by Django 4.2.14 on 2024-08-04 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_alter_flightmodel_departing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelclassmodel',
            name='name',
            field=models.CharField(choices=[('Economy', 'Economy class'), ('Business', 'Business class'), ('First', 'First class')], default='Economy', max_length=128),
        ),
    ]
