# Generated by Django 3.0.4 on 2020-03-17 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='question_text',
        ),
    ]
