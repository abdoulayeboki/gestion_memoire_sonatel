# Generated by Django 3.1.6 on 2021-03-31 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0007_auto_20210331_1907'),
        ('sujet_module', '0002_auto_20210331_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='sujet',
            name='personnesPostulant',
            field=models.ManyToManyField(related_name='sujetsPostuler', through='sujet_module.SujetPostuler', to='administration.Personnel'),
        ),
        migrations.AlterField(
            model_name='sujetpostuler',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.personnel'),
        ),
        migrations.AlterField(
            model_name='sujetpostuler',
            name='sujet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sujet_module.sujet'),
        ),
    ]