# Generated by Django 2.1.8 on 2019-10-04 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Failure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('challenge', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='challenges.Challenge')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='failure', to='teams.Team')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]