# Generated by Django 4.1.3 on 2022-11-16 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_extenduser_email_alter_extenduser_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='no_image.png', upload_to='media'),
        ),
    ]