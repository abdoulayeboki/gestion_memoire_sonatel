# Generated by Django 3.1.6 on 2021-04-27 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sujet_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encadrement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appreciation', models.CharField(max_length=255)),
                ('dateDebutEncadrement', models.DateTimeField(auto_now_add=True)),
                ('dateFinEncadrement', models.DateTimeField(auto_now_add=True)),
                ('sujet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='encadrement', to='sujet_module.sujet')),
            ],
        ),
    ]
