# Generated by Django 3.2 on 2021-07-17 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_question_competition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='competition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.competition'),
        ),
    ]