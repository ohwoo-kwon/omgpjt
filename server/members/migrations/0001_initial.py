# Generated by Django 3.2.4 on 2021-06-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('e_name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('birth', models.DateField()),
                ('youtube', models.URLField(blank=True)),
                ('instagram', models.URLField()),
                ('profile', models.URLField()),
                ('position', models.ManyToManyField(to='members.Position')),
            ],
        ),
    ]
