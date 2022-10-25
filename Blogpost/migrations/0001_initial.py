# Generated by Django 4.1.2 on 2022-10-25 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importance', models.CharField(choices=[('LW', 'Low'), ('IM', 'Intermediate'), ('HH', 'High')], default='LW', max_length=2)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
