# Generated by Django 4.1.1 on 2022-09-25 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_answer_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='text',
            new_name='body',
        ),
    ]
