# Generated by Django 4.0.2 on 2022-02-12 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='InputForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('contact_number', models.IntegerField()),
                ('International_code', models.IntegerField()),
                ('business_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input_form.businesstype')),
            ],
        ),
    ]
