# Generated by Django 3.1.6 on 2021-04-27 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encadrement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encadrement',
            name='dateFinEncadrement',
            field=models.DateTimeField(null=True),
        ),
    ]