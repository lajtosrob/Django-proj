# Generated by Django 4.2.1 on 2023-05-10 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Szemely',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vezeteknev', models.CharField(max_length=100)),
                ('keresztnev', models.CharField(max_length=100)),
                ('eletkor', models.IntegerField()),
                ('hazas', models.BooleanField(default=False)),
                ('elettortenet', models.TextField()),
                ('letrehozva', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
