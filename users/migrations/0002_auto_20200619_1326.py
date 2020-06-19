# Generated by Django 3.0.5 on 2020-06-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igarden', '0002_delete_userflowerslist'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favourites',
            field=models.ManyToManyField(related_name='favoured_by', to='igarden.Flower'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_default.jpg', upload_to='profile_pics'),
        ),
    ]
