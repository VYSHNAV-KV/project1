# Generated by Django 5.1.1 on 2024-10-27 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='signupdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
                ('Re_password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
