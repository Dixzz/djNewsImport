# Generated by Django 4.2.13 on 2024-06-18 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('intensity', models.IntegerField()),
                ('likelihood', models.IntegerField()),
                ('relevance', models.IntegerField()),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('region', models.CharField(blank=True, max_length=100)),
                ('pestle', models.CharField(max_length=100)),
            ],
        ),
    ]