# Generated by Django 2.0.3 on 2018-04-12 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityHotplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_usable', models.BooleanField(default=True, verbose_name='사용여부')),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modify_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
                ('name', models.CharField(max_length=20, verbose_name='핫플레이스')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CityInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_usable', models.BooleanField(default=True, verbose_name='사용여부')),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modify_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
                ('name', models.CharField(max_length=20, verbose_name='도시명')),
                ('continent', models.CharField(max_length=20, verbose_name='대륙')),
                ('nationality', models.CharField(max_length=20, verbose_name='나라')),
                ('city_image', models.ImageField(upload_to='city', verbose_name='도시이미지')),
                ('city_image_thumbnail', models.ImageField(upload_to='city-thumbnail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_usable', models.BooleanField(default=True, verbose_name='사용여부')),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modify_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
                ('name', models.CharField(max_length=50, verbose_name='회사명')),
                ('info', models.TextField(verbose_name='회사설명')),
                ('company_image', models.ImageField(upload_to='company', verbose_name='회사이미지')),
                ('company_image_thumbnail', models.ImageField(upload_to='company-thumbnail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TravelInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_usable', models.BooleanField(default=True, verbose_name='사용여부')),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modify_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
                ('travel_id', models.IntegerField(verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='상품명')),
                ('category', models.CharField(blank=True, choices=[('ticket', '교통/티켓'), ('convenience', '여행편의'), ('guide_tour', '가이드투어'), ('restaurant', '식당'), ('activity', '액티비티'), ('accomodation', '숙박/민박'), ('enjoy', '즐길거리')], max_length=40, verbose_name='카테고리')),
                ('theme', models.CharField(blank=True, max_length=100, verbose_name='테마')),
                ('product_type', models.CharField(blank=True, max_length=100, verbose_name='상품타입')),
                ('language', models.CharField(max_length=40, verbose_name='언어')),
                ('time', models.CharField(max_length=40, verbose_name='소요시간')),
                ('description', models.TextField(verbose_name='상품설명')),
                ('meeting_time', models.CharField(max_length=100, verbose_name='만남시간')),
                ('meeting_place', models.CharField(max_length=100, verbose_name='만남장소')),
                ('price', models.IntegerField(default=0, verbose_name='상품금액')),
                ('price_descrption', models.TextField(verbose_name='상품금액 포함사항')),
                ('maxPeople', models.IntegerField(default=0, verbose_name='최대 사람 수')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.CityInformation', verbose_name='city')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.CompanyInformation', verbose_name='company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TravelInformationImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_usable', models.BooleanField(default=True, verbose_name='사용여부')),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modify_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
                ('image_id', models.IntegerField(verbose_name='이미지 ID')),
                ('product_image', models.ImageField(upload_to='product', verbose_name='상품이미지')),
                ('product_image_thumbnail', models.ImageField(upload_to='product-thumbnail')),
                ('travel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='travel.TravelInformation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TravelSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_usable', models.BooleanField(default=True, verbose_name='사용여부')),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modify_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
                ('reserved_people', models.IntegerField(default=0)),
                ('start_date', models.DateField(verbose_name='여행시작날짜')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='여행끝날짜')),
                ('travel_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.TravelInformation', verbose_name='travel_info')),
                ('travelschedule_user', models.ManyToManyField(through='reservation.Reservation', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-creation_datetime'],
            },
        ),
        migrations.AddField(
            model_name='cityhotplace',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.CityInformation', verbose_name='city'),
        ),
    ]
