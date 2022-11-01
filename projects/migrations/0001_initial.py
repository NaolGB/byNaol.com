# Generated by Django 4.0 on 2022-10-31 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=128)),
                ('project_media', models.ImageField(upload_to='')),
                ('project_description', models.TextField()),
                ('project_detail', models.TextField()),
                ('project_repo', models.URLField()),
            ],
        ),
    ]
