# Generated by Django 3.1.6 on 2021-02-17 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_etudiant_telephon'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='email',
            field=models.CharField(default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='telephon',
            field=models.CharField(default=None, max_length=18),
        ),
    ]
