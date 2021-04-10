# Generated by Django 3.1.6 on 2021-04-10 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0007_auto_20210331_1907'),
        ('sujet_module', '0007_auto_20210401_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='SujetValider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateValider', models.DateTimeField(auto_now_add=True)),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.personnel')),
                ('sujet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sujet_module.sujet')),
            ],
            options={
                'unique_together': {('sujet', 'personnel')},
            },
        ),
        migrations.AddField(
            model_name='sujet',
            name='personnelValider',
            field=models.ManyToManyField(through='sujet_module.SujetValider', to='administration.Personnel'),
        ),
    ]