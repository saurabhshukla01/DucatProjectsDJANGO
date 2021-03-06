# Generated by Django 2.1.3 on 2019-02-13 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proff_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=30)),
                ('proff_fee', models.IntegerField()),
                ('proff_image', models.ImageField(upload_to='Proff_name')),
            ],
        ),
        migrations.CreateModel(
            name='University_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('University_name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('contact_no', models.CharField(blank=True, max_length=10, null=True)),
                ('image', models.ImageField(upload_to='University_name')),
            ],
        ),
        migrations.AddField(
            model_name='proff_name',
            name='Proff_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineportal.University_name'),
        ),
    ]
