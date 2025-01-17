# Generated by Django 3.2.6 on 2021-08-25 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karate', '0003_auto_20210823_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='about_belt',
        ),
        migrations.RemoveField(
            model_name='info',
            name='belt_img',
        ),
        migrations.RemoveField(
            model_name='info',
            name='kyu',
        ),
        migrations.AddField(
            model_name='belt',
            name='about_belt',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='belt',
            name='belt_img',
            field=models.ImageField(null=True, upload_to='', verbose_name='photos/'),
        ),
        migrations.AddField(
            model_name='belt',
            name='kyu',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
