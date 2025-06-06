# Generated by Django 5.1.7 on 2025-03-15 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='full_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='volunteer_pics/'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
