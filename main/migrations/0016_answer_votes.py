# Generated by Django 4.1.1 on 2022-09-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_answer_options_remove_answer_votesdown_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
