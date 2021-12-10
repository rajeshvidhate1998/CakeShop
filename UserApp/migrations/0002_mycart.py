# Generated by Django 3.1.7 on 2021-03-16 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.cake')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.userinfo')),
            ],
            options={
                'db_table': 'MyCart',
            },
        ),
    ]
