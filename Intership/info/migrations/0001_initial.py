# Generated by Django 4.2.14 on 2024-07-25 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('hotel', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('price', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Ticket',
            },
        ),
    ]
