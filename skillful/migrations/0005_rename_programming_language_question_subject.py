# Generated by Django 4.0.4 on 2022-05-11 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skillful', '0004_alter_subject_image_alter_test_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='programming_language',
            new_name='subject',
        ),
    ]
