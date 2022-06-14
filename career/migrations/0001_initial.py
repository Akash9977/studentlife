# Generated by Django 4.0.1 on 2022-03-22 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30)),
                ('semail', models.EmailField(max_length=30)),
                ('scell', models.CharField(max_length=15)),
                ('sdepartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.department')),
                ('sgender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.gender')),
            ],
        ),
    ]