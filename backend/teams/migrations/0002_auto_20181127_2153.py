# Generated by Django 2.1.2 on 2018-11-27 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='affiliation',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]