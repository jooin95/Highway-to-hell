# Generated by Django 2.2 on 2019-05-16 07:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190419_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('feedback', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='new', max_length=20)),
                ('adminComment', models.TextField(null=True)),
                ('ipAddress', models.CharField(max_length=20)),
                ('deviceInfo', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelTable(
            name='dalabtest',
            table='new_collect',
        ),
    ]
