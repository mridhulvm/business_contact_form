# Generated by Django 4.0.2 on 2022-02-12 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstype',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='businesstype',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='inputform',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='inputform',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
