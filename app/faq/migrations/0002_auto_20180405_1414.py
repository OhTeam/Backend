# Generated by Django 2.0.3 on 2018-04-05 05:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('isusable', models.BooleanField(default=True, verbose_name='사용여부')),
                ('creationdatetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modifydatetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
            ],
        ),
        migrations.DeleteModel(
            name='HomepageInfomation',
        ),
    ]
