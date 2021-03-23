# Generated by Django 3.1.6 on 2021-03-22 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sujet_module', '0002_auto_20210322_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sujet',
            name='etatSujet',
            field=models.CharField(choices=[('PROPOSE', 'PROPOSE'), ('ACCORDE', 'ACCORDE'), ('VALIDE', 'VALIDE'), ('TERMINE', 'TERMINE'), ('SOUTENU', 'SOUTENU'), ('DEPOSE', 'DEPOSE')], default='PROPOSE', max_length=10),
        ),
        migrations.AlterField(
            model_name='sujet',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sujets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]