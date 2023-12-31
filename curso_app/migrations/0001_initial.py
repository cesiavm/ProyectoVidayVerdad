# Generated by Django 4.2.7 on 2023-11-01 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id_nivel', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_nivel', models.CharField(max_length=50, verbose_name='Nombre Nivel')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'nivel',
            },
        ),
        migrations.CreateModel(
            name='Trimestre',
            fields=[
                ('id_trimestre', models.AutoField(primary_key=True, serialize=False)),
                ('numero_trimestre', models.CharField(max_length=30, verbose_name='Trimestre')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'trimestre',
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id_turno', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_turno', models.CharField(max_length=30)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'turno',
            },
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id_grado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_grado', models.CharField(max_length=50)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('nivel', models.ForeignKey(db_column='nivel', on_delete=django.db.models.deletion.CASCADE, to='curso_app.nivel')),
            ],
            options={
                'db_table': 'grado',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('capacidad_estudiantes', models.IntegerField()),
                ('cantidad_estudiantes', models.IntegerField(default=0)),
                ('cantidad_asignaturas', models.IntegerField()),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('grado', models.ForeignKey(db_column='grado', on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='curso_app.grado')),
                ('turno', models.ForeignKey(db_column='turno', on_delete=django.db.models.deletion.CASCADE, to='curso_app.turno')),
            ],
            options={
                'db_table': 'curso',
            },
        ),
    ]
