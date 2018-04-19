# Generated by Django 2.0.3 on 2018-04-16 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('travel', '0001_initial'),
        ('reservation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='wishtravel',
            name='travel_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wish_user_info_list', to='travel.TravelInformation'),
        ),
        migrations.AddField(
            model_name='wishtravel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wish_products_info_list', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reservation',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='travel_schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.TravelSchedule', verbose_name='travel_schedule'),
        ),
        migrations.AddField(
            model_name='recentvisitpage',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recentvisitpage',
            name='travel_schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.TravelInformation'),
        ),
        migrations.AlterUniqueTogether(
            name='wishtravel',
            unique_together={('travel_info', 'user')},
        ),
    ]
