# Generated by Django 4.2.1 on 2024-03-05 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpapp', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='activate',
            new_name='active',
        ),
    ]
