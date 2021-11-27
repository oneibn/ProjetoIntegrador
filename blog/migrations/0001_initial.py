# Generated by Django 3.2.9 on 2021-11-25 02:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('assunto', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mensagem', models.TextField(max_length=1000)),
                ('data_post', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]