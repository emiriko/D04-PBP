# Generated by Django 4.1.2 on 2022-10-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogpost', '0007_alter_blogpostmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostmodel',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
