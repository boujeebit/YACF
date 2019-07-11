# Generated by Django 2.1.5 on 2019-07-11 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=1000)),
                ('points', models.IntegerField(default=0)),
                ('flag', models.CharField(max_length=100)),
                ('show', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='challenges', to='categories.Category')),
            ],
        ),
    ]
