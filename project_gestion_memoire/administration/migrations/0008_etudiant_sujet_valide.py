# Generated by Django 3.1.6 on 2021-04-14 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0007_auto_20210331_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='sujet_valide',
            field=models.BooleanField(default=False),
        ),
    ]
