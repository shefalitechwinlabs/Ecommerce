# Generated by Django 4.1.3 on 2022-11-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_extenduser_bio_remove_extenduser_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenduser',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='extenduser',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
