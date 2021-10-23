# Generated by Django 3.2.8 on 2021-10-23 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211023_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(max_length=100)),
                ('q1_opt_1', models.CharField(max_length=100)),
                ('q1_opt_2', models.CharField(max_length=100)),
                ('q1_opt_3', models.CharField(max_length=100)),
                ('q1_ans', models.CharField(max_length=100)),
                ('q2', models.CharField(max_length=100)),
                ('q2_opt_1', models.CharField(max_length=100)),
                ('q2_opt_2', models.CharField(max_length=100)),
                ('q2_opt_3', models.CharField(max_length=100)),
                ('q2_ans', models.CharField(max_length=100)),
                ('q3', models.CharField(max_length=100)),
                ('q3_opt_1', models.CharField(max_length=100)),
                ('q3_opt_2', models.CharField(max_length=100)),
                ('q3_opt_3', models.CharField(max_length=100)),
                ('q3_ans', models.CharField(max_length=100)),
                ('q4', models.CharField(max_length=100)),
                ('q4_opt_1', models.CharField(max_length=100)),
                ('q4_opt_2', models.CharField(max_length=100)),
                ('q4_opt_3', models.CharField(max_length=100)),
                ('q4_ans', models.CharField(max_length=100)),
                ('q5', models.CharField(max_length=100)),
                ('q5_opt_1', models.CharField(max_length=100)),
                ('q5_opt_2', models.CharField(max_length=100)),
                ('q5_opt_3', models.CharField(max_length=100)),
                ('q5_ans', models.CharField(max_length=100)),
                ('q6', models.CharField(max_length=100)),
                ('q6_opt_1', models.CharField(max_length=100)),
                ('q6_opt_2', models.CharField(max_length=100)),
                ('q6_opt_3', models.CharField(max_length=100)),
                ('q6_ans', models.CharField(max_length=100)),
                ('q7', models.CharField(max_length=100)),
                ('q7_opt_1', models.CharField(max_length=100)),
                ('q7_opt_2', models.CharField(max_length=100)),
                ('q7_opt_3', models.CharField(max_length=100)),
                ('q7_ans', models.CharField(max_length=100)),
                ('q8', models.CharField(max_length=100)),
                ('q8_opt_1', models.CharField(max_length=100)),
                ('q8_opt_2', models.CharField(max_length=100)),
                ('q8_opt_3', models.CharField(max_length=100)),
                ('q8_ans', models.CharField(max_length=100)),
                ('q9', models.CharField(max_length=100)),
                ('q9_opt_1', models.CharField(max_length=100)),
                ('q9_opt_2', models.CharField(max_length=100)),
                ('q9_opt_3', models.CharField(max_length=100)),
                ('q9_ans', models.CharField(max_length=100)),
                ('q10', models.CharField(max_length=100)),
                ('q10_opt_1', models.CharField(max_length=100)),
                ('q10_opt_2', models.CharField(max_length=100)),
                ('q10_opt_3', models.CharField(max_length=100)),
                ('q10_ans', models.CharField(max_length=100)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.quiz')),
            ],
            options={
                'verbose_name_plural': 'Quiz Qestions',
            },
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]