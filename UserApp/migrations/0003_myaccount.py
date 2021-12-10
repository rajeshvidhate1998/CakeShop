# Generated by Django 3.1.7 on 2021-03-18 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_mycart'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardno', models.CharField(max_length=16)),
                ('cvv', models.CharField(max_length=4)),
                ('expiry', models.CharField(max_length=10)),
                ('balance', models.FloatField(default=10000)),
            ],
            options={
                'db_table': 'MyAccount',
            },
        ),
    ]