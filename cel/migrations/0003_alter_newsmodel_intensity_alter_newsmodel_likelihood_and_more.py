# Generated by Django 4.2.13 on 2024-06-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cel', '0002_newsmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='intensity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='likelihood',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='relevance',
            field=models.IntegerField(null=True),
        ),
    ]
