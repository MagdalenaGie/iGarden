# Generated by Django 3.0.5 on 2020-05-25 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_favouriteslist'),
        ('users', '0002_profile_fav_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fav_list',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='lists.FavouritesList'),
        ),
    ]