# Generated by Django 4.0.4 on 2022-05-11 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillful', '0003_alter_test_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='test',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]