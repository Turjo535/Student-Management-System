# Generated by Django 5.0 on 2025-03-25 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_model',
            old_name='emal',
            new_name='email',
        ),
    ]
