# Generated by Django 4.0.4 on 2022-05-11 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillful', '0007_alter_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(help_text='Text of the Question', max_length=250, verbose_name='Text'),
        ),
    ]