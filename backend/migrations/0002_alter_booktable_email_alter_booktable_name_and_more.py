# Generated by Django 4.0.4 on 2022-05-30 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktable',
            name='email',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='booktable',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='category',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
