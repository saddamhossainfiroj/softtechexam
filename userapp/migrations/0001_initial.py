# Generated by Django 2.0.3 on 2020-09-28 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('user_pass', models.CharField(max_length=200)),
                ('user_img', models.ImageField(upload_to='user_images')),
                ('insert_date', models.DateTimeField(auto_now_add=True)),
                ('user_type', models.CharField(choices=[('user', 'user'), ('admin', 'admin')], max_length=20)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('insert_by', models.IntegerField(default=0)),
                ('update_by', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'User Registration',
                'verbose_name_plural': 'User Registration',
            },
        ),
    ]