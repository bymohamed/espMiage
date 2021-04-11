# Generated by Django 3.1.6 on 2021-02-08 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.FloatField(blank=True)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('idmachine', models.IntegerField()),
            ],
        ),
    ]