# Generated by Django 4.1.4 on 2023-05-10 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_remove_user_pic_post_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pic',
        ),
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.CharField(default='https://www.kindpng.com/picc/m/24-248253_user-profile-default-image-png-clipart-png-download.png', max_length=500),
        ),
    ]
