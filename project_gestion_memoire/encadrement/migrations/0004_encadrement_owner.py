# Generated by Django 3.1.6 on 2021-04-27 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
        ('encadrement', '0003_evenement_ressource'),
    ]

    operations = [
        migrations.AddField(
            model_name='encadrement',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='encadrements', to='administration.personnel'),
            preserve_default=False,
        ),
    ]
