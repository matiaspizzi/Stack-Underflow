# Generated by Django 4.1.1 on 2022-09-25 20:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_alter_answer_options_answer_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='voters',
            field=models.ManyToManyField(blank=True, related_name='AnswerVoters', to=settings.AUTH_USER_MODEL),
        ),
    ]
