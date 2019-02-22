# Generated by Django 2.1.3 on 2019-02-14 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineportal', '0002_auto_20190213_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='proff_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proff_name', models.CharField(max_length=30)),
                ('proff_salary', models.IntegerField()),
                ('proff_email', models.EmailField(max_length=30)),
                ('proff_address', models.CharField(max_length=30)),
                ('proff_lacture_fee', models.IntegerField(max_length=30)),
                ('proff_image', models.ImageField(upload_to='proff_of_university')),
            ],
        ),
        migrations.CreateModel(
            name='proff_of_university',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proff_name', models.CharField(max_length=30)),
                ('proff_salary', models.IntegerField()),
                ('proff_image', models.ImageField(upload_to='proff_of_university')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('University_name', models.CharField(max_length=30)),
                ('University_location', models.CharField(max_length=30)),
                ('University_contacts', models.CharField(blank=True, max_length=10, null=True)),
                ('University_image', models.ImageField(upload_to='University')),
            ],
        ),
        migrations.RemoveField(
            model_name='proff_name',
            name='Proff',
        ),
        migrations.DeleteModel(
            name='Proff_name',
        ),
        migrations.DeleteModel(
            name='University_name',
        ),
        migrations.AddField(
            model_name='proff_of_university',
            name='proff_of_university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineportal.University'),
        ),
        migrations.AddField(
            model_name='proff_details',
            name='proff_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineportal.proff_of_university'),
        ),
    ]
