# Generated by Django 4.1.3 on 2023-01-06 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyProject',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=130)),
                ('views', models.IntegerField(default=0)),
                ('timesp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
