# Generated by Django 4.1.1 on 2022-09-25 11:16

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
