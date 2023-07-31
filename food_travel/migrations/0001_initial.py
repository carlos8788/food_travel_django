# Generated by Django 4.2.3 on 2023-07-30 18:56

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinoCulinario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('tipo_cocina', models.CharField(max_length=255)),
                ('ingredientes', models.CharField(blank=True, max_length=255)),
                ('precio_minimo', models.FloatField()),
                ('precio_maximo', models.FloatField()),
                ('popularidad', models.FloatField()),
                ('disponibilidad', models.BooleanField(default=True)),
                ('imagen', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RutaVisita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('destinos', models.ManyToManyField(to='food_travel.destinoculinario')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('latitud', models.CharField(max_length=255)),
                ('longitud', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('historial_rutas', models.ManyToManyField(blank=True, to='food_travel.rutavisita')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField()),
                ('comentario', models.TextField()),
                ('animo', models.CharField(choices=[('Positivo', 'Positivo'), ('Negativo', 'Negativo')], max_length=8)),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_travel.destinoculinario')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_travel.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='destinoculinario',
            name='ubicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_travel.ubicacion'),
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('hora_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_travel.destinoculinario')),
            ],
        ),
    ]
