# Generated by Django 4.1.2 on 2022-10-15 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='Username',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Username',
            new_name='username',
        ),
    ]
