# Generated by Django 3.0.4 on 2020-04-06 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=40)),
                ('event_description', models.CharField(max_length=400)),
                ('event_start_date', models.DateField()),
                ('event_end_date', models.DateField()),
                ('verified', models.BooleanField(default=False)),
                ('ended', models.BooleanField(default=False)),
                ('max_participants', models.PositiveIntegerField(null=True)),
                ('num_participants', models.PositiveIntegerField(default=0)),
                ('max_waiting_list_size', models.PositiveIntegerField(null=True)),
                ('num_in_waiting_list', models.PositiveIntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_created+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WaitingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_time', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waiting_list+', to='event.Event')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_waiting+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants+', to='event.Event')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_registered+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
