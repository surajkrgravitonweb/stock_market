# Generated by Django 3.2.8 on 2023-09-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountReigster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('pancard', models.CharField(max_length=200)),
                ('bankaccount', models.CharField(max_length=200)),
                ('ifsccode', models.CharField(max_length=200)),
                ('aadhaarCardNumber', models.CharField(max_length=200)),
            ],
        ),
    ]