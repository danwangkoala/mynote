# Generated by Django 2.2.4 on 2020-05-12 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200512_0320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='categroy',
            new_name='category',
        ),
    ]