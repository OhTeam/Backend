# Generated by Django 2.0.3 on 2018-04-13 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180413_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimage',
            name='blog_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.Blog'),
        ),
    ]
