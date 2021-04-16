# Generated by Django 3.1.6 on 2021-04-16 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25, unique=True)),
                ('nom', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filieres', to='administration.departement')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('cni', models.CharField(max_length=20, unique=True)),
                ('telephon', models.CharField(default=None, max_length=18)),
                ('email', models.CharField(max_length=100)),
                ('profil', models.CharField(choices=[('ETUDIANT', 'ETUDIANT'), ('ENSEIGNANT', 'ENSEIGNANT'), ('AUTRE', 'AUTRE')], default='AUTRE', max_length=20)),
                ('nbr_sujet_valide', models.IntegerField(default=0)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personnel', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('cni',), ('user',)},
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25, unique=True)),
                ('nom', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25, unique=True)),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('niveau', models.CharField(choices=[('BTS', 'BTS'), ('L3', 'licence 3'), ('M2', 'Master 2'), ('T1', 'These 1'), ('T2', 'These 2'), ('T3', 'These 3')], default='M2', max_length=10)),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialites', to='administration.filiere')),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25, unique=True)),
                ('anneeScolaire', models.CharField(choices=[('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024'), ('2024-2025', '2024-2025'), ('2025-2026', '2025-2026')], default='2021', max_length=9)),
                ('specialite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='administration.specialite')),
            ],
            options={
                'unique_together': {('anneeScolaire', 'specialite')},
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('personnel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administration.personnel')),
                ('ine', models.CharField(max_length=7, unique=True)),
                ('classe', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='etudiants', to='administration.classe')),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etudiants', to='administration.promotion')),
            ],
            bases=('administration.personnel',),
        ),
        migrations.CreateModel(
            name='Enseignent',
            fields=[
                ('personnel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administration.personnel')),
                ('grade', models.CharField(max_length=100)),
                ('specialite', models.CharField(max_length=100)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professeurs', to='administration.departement')),
            ],
            bases=('administration.personnel',),
        ),
    ]
