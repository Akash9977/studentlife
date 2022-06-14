# Generated by Django 4.0.1 on 2022-04-04 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='scell',
            new_name='Cell',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='sdepartment',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='semail',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='sgender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='sname',
            new_name='Name',
        ),
        migrations.AddField(
            model_name='student',
            name='Picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='student',
            name='YourMessage',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]