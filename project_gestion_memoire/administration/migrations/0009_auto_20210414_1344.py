# Generated by Django 3.1.6 on 2021-04-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0008_etudiant_sujet_valide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='sujet_valide',
        ),
        migrations.AddField(
            model_name='personnel',
            name='sujet_valide',
            field=models.BooleanField(default=False),
        ),
    ]
