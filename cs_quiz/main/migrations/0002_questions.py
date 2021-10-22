# Generated by Django 3.2.8 on 2021-10-22 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('opt_1', models.CharField(max_length=100)),
                ('opt_2', models.CharField(max_length=100)),
                ('opt_3', models.CharField(max_length=100)),
                ('opt_4', models.CharField(max_length=100)),
                ('ans', models.CharField(max_length=100)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.quizes')),
            ],
        ),
    ]