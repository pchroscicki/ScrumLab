# Generated by Django 4.0.3 on 2022-03-15 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0002_alter_recipe_created_alter_recipe_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(null=True)),
                ('created', models.DateTimeField(default=datetime.date.today)),
                ('updated', models.DateTimeField(default=datetime.date.today)),
            ],
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]