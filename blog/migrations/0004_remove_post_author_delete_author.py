# Generated by Django 4.1.7 on 2023-02-23 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_author_alter_post_category_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]