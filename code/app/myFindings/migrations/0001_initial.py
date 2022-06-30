# Generated by Django 4.0.5 on 2022-06-29 23:47

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import myFindings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuiltMaterial',
            fields=[
                ('nombre', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'material construido',
                'verbose_name_plural': 'materiales construidos',
            },
        ),
        migrations.CreateModel(
            name='Excavation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre de la excavación')),
                ('n_excavacion', models.CharField(help_text='Ej. 001, 002, 003, etc', max_length=3, unique=True, validators=[myFindings.models.validate_number], verbose_name='Número de excavación')),
                ('latitud', models.FloatField(blank=True, null=True)),
                ('longitud', models.FloatField(blank=True, null=True)),
                ('altura', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'excavación',
                'verbose_name_plural': 'excavaciones',
            },
        ),
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letra', models.CharField(choices=[('MR', 'Muro'), ('SL', 'Suelo'), ('PO', 'Pozo'), ('FS', 'Fosa'), ('SI', 'Silo'), ('PR', 'Puerta'), ('CN', 'Canalización'), ('DP', 'Depósito'), ('TN', 'Tinaja'), ('ES', 'Sin identificación')], max_length=2)),
                ('numero', models.CharField(max_length=6, verbose_name='Número (UE que lo identifica)')),
                ('fase', models.CharField(blank=True, choices=[('A: época contemporánea', (('A1', 'A1: Siglo XVIII'), ('A2', 'A2: Siglo XIX'), ('A3', 'A3: Siglo XX'))), ('B: época moderna', (('B1', 'B1: Siglo XV'), ('B2', 'B2: Siglo XVI'), ('B3', 'B3: Siglo XVII'))), ('C: época medieval', (('C1', 'C1: fase emiral'), ('C2', 'C2: fase califal'), ('C3', 'C3: fase taifas'), ('C4', 'C4: fase almorávide/almohade'), ('C5', 'C5: fase nazarí'))), ('D: época romana', (('D1', 'D1: época republicana'), ('D2', 'D2: Alto Imperio'), ('D3', 'D3: Bajo Imperio'), ('D4', 'D4: Antigüedad tardía'))), ('E: época ibérica', (('E1', 'E1: Protoibérico-orientalizante'), ('E2', 'E2: Ibérico antiguo'), ('E3', 'E3: Ibérico pleno'), ('E4', 'E4: Ibérico tardío o final'))), ('F: Edad del Bronce', (('F1', 'F1: Bronce Antiguo'), ('F2', 'F2: Bronce Pleno'), ('F3', 'F3: Bronce Tardío'), ('F4', 'F4: Bronce Final')))], max_length=2, null=True)),
                ('tpq', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Terminus Post Quem (TPQ)')),
                ('taq', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Terminus Ante Quem (TAQ)')),
                ('definicion', models.CharField(blank=True, max_length=100, null=True)),
                ('comentarios', models.CharField(blank=True, max_length=100, null=True)),
                ('sector', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número de sector')),
                ('zona', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número de zona')),
                ('año', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('estructura', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número de estructura')),
                ('croquis_plan', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Croquis del plan')),
                ('croquis_seccion', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Croquis de la sección')),
            ],
            options={
                'verbose_name': 'hecho',
                'verbose_name_plural': 'hechos',
            },
        ),
        migrations.CreateModel(
            name='Inclusion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Cenizas', 'Cenizas'), ('Carbones', 'Carbones'), ('Huesos', 'Huesos'), ('Adobe', 'Adobe'), ('Cañizo', 'Cañizo'), ('Tejas', 'Tejas'), ('Bloques', 'Bloques'), ('Cal', 'Cal'), ('Mortero', 'Mortero'), ('Enlucido', 'Enlucido')], max_length=10)),
                ('frecuencia', models.CharField(blank=True, choices=[('Ausencia', 'Ausencia'), ('Ocasional', 'Ocasional'), ('Medio', 'Medio'), ('Frecuente', 'Frecuente')], max_length=10, null=True)),
                ('grosor', models.CharField(blank=True, choices=[('< 2 cm', '< 2 cm'), ('2-6 cm', '2-6 cm'), ('6-12 cm', '6-12 cm'), ('> 12 cm', '> 12 cm')], max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'inclusión',
                'verbose_name_plural': 'inclusiones',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('date_and_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_estancia', models.CharField(help_text='Ej. 001, 002, 003, etc', max_length=3, unique=True, validators=[myFindings.models.validate_number], verbose_name='Número de estancia')),
                ('n_zona', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número de zona')),
                ('n_sector', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número de sector')),
                ('observaciones', models.CharField(blank=True, max_length=200, null=True)),
                ('croquis_planta', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Croquis de la planta')),
                ('n_planta', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número de planta')),
                ('n_seccion', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número de sección')),
                ('elevacion', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número de elevación')),
                ('tpq', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Terminus Post Quem (TPQ)')),
                ('taq', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Terminus Ante Quem (TAQ)')),
                ('fase', models.CharField(blank=True, choices=[('A: época contemporánea', (('A1', 'A1: Siglo XVIII'), ('A2', 'A2: Siglo XIX'), ('A3', 'A3: Siglo XX'))), ('B: época moderna', (('B1', 'B1: Siglo XV'), ('B2', 'B2: Siglo XVI'), ('B3', 'B3: Siglo XVII'))), ('C: época medieval', (('C1', 'C1: fase emiral'), ('C2', 'C2: fase califal'), ('C3', 'C3: fase taifas'), ('C4', 'C4: fase almorávide/almohade'), ('C5', 'C5: fase nazarí'))), ('D: época romana', (('D1', 'D1: época republicana'), ('D2', 'D2: Alto Imperio'), ('D3', 'D3: Bajo Imperio'), ('D4', 'D4: Antigüedad tardía'))), ('E: época ibérica', (('E1', 'E1: Protoibérico-orientalizante'), ('E2', 'E2: Ibérico antiguo'), ('E3', 'E3: Ibérico pleno'), ('E4', 'E4: Ibérico tardío o final'))), ('F: Edad del Bronce', (('F1', 'F1: Bronce Antiguo'), ('F2', 'F2: Bronce Pleno'), ('F3', 'F3: Bronce Tardío'), ('F4', 'F4: Bronce Final')))], max_length=2, null=True)),
                ('periodo', models.CharField(blank=True, choices=[('Siglo XVIII', 'Contemporánea: Siglo XVIII'), ('Siglo XIX', 'Contemporánea: Siglo XIX'), ('Siglo XX', 'Contemporánea: Siglo XX'), ('Siglo XV', 'Moderna: Siglo XV'), ('Siglo XVI', 'Moderna: Siglo XVI'), ('Siglo XVII', 'Moderna: Siglo XVII'), ('Fase emiral', 'Medieval: emiral'), ('Fase califal', 'Medieval: califal'), ('Fase taifas', 'Medieval: taifas'), ('Fase invasiones almorávides y almohades', 'Medieval: almorávide/almohade'), ('Fase nazarí', 'Medieval: nazarí'), ('Fase republicana', 'Romana: época republicana'), ('Fase Altoimperial', 'Romana: Alto Imperio'), ('Fase Bajoimperial', 'Romana: Bajo Imperio'), ('Antigüedad tardía', 'Romana: Antigüedad tardía'), ('Protoibérico-orientalizante', 'Ibérica: Protoibérico'), ('Ibérico antiguo', 'Ibérica: Ibérico antiguo'), ('Ibérico pleno', 'Ibérica: Ibérico pleno'), ('Ibérico final', 'Ibérica: Ibérico tardío o final'), ('Bronce antiguo', 'Edad del Bronce: Antiguo'), ('Bronce pleno', 'Edad del Bronce: Pleno'), ('Bronce tardío', 'Edad del Bronce: Tardío'), ('Bronce final', 'Edad del Bronce: Final')], max_length=100, null=True)),
                ('autor', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'estancia',
                'verbose_name_plural': 'estancias',
            },
        ),
        migrations.CreateModel(
            name='SedimentaryMaterial',
            fields=[
                ('nombre', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'material sedimentario',
                'verbose_name_plural': 'materiales sedimentarios',
            },
        ),
        migrations.CreateModel(
            name='UE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=6)),
                ('n_orden', models.CharField(help_text='Ej. 001, 002, 003, etc', max_length=3, validators=[myFindings.models.validate_number], verbose_name='Número de orden')),
                ('plano_n', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número de plano')),
                ('seccion_n', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número de sección')),
                ('elevacion_n', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número de elevación')),
                ('croquis_planta', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Croquis de la planta')),
                ('croquis_seccion', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Croquis de la sección')),
                ('tpq', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Terminus Post Quem (TPQ)')),
                ('taq', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Terminus Ante Quem (TAQ)')),
                ('fase', models.CharField(blank=True, choices=[('A: época contemporánea', (('A1', 'A1: Siglo XVIII'), ('A2', 'A2: Siglo XIX'), ('A3', 'A3: Siglo XX'))), ('B: época moderna', (('B1', 'B1: Siglo XV'), ('B2', 'B2: Siglo XVI'), ('B3', 'B3: Siglo XVII'))), ('C: época medieval', (('C1', 'C1: fase emiral'), ('C2', 'C2: fase califal'), ('C3', 'C3: fase taifas'), ('C4', 'C4: fase almorávide/almohade'), ('C5', 'C5: fase nazarí'))), ('D: época romana', (('D1', 'D1: época republicana'), ('D2', 'D2: Alto Imperio'), ('D3', 'D3: Bajo Imperio'), ('D4', 'D4: Antigüedad tardía'))), ('E: época ibérica', (('E1', 'E1: Protoibérico-orientalizante'), ('E2', 'E2: Ibérico antiguo'), ('E3', 'E3: Ibérico pleno'), ('E4', 'E4: Ibérico tardío o final'))), ('F: Edad del Bronce', (('F1', 'F1: Bronce Antiguo'), ('F2', 'F2: Bronce Pleno'), ('F3', 'F3: Bronce Tardío'), ('F4', 'F4: Bronce Final')))], max_length=2, null=True)),
                ('periodo', models.CharField(blank=True, choices=[('Siglo XVIII', 'Contemporánea: Siglo XVIII'), ('Siglo XIX', 'Contemporánea: Siglo XIX'), ('Siglo XX', 'Contemporánea: Siglo XX'), ('Siglo XV', 'Moderna: Siglo XV'), ('Siglo XVI', 'Moderna: Siglo XVI'), ('Siglo XVII', 'Moderna: Siglo XVII'), ('Fase emiral', 'Medieval: emiral'), ('Fase califal', 'Medieval: califal'), ('Fase taifas', 'Medieval: taifas'), ('Fase invasiones almorávides y almohades', 'Medieval: almorávide/almohade'), ('Fase nazarí', 'Medieval: nazarí'), ('Fase republicana', 'Romana: época republicana'), ('Fase Altoimperial', 'Romana: Alto Imperio'), ('Fase Bajoimperial', 'Romana: Bajo Imperio'), ('Antigüedad tardía', 'Romana: Antigüedad tardía'), ('Protoibérico-orientalizante', 'Ibérica: Protoibérico'), ('Ibérico antiguo', 'Ibérica: Ibérico antiguo'), ('Ibérico pleno', 'Ibérica: Ibérico pleno'), ('Ibérico final', 'Ibérica: Ibérico tardío o final'), ('Bronce antiguo', 'Edad del Bronce: Antiguo'), ('Bronce pleno', 'Edad del Bronce: Pleno'), ('Bronce tardío', 'Edad del Bronce: Tardío'), ('Bronce final', 'Edad del Bronce: Final')], max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, max_length=200, null=True)),
                ('autor', models.CharField(blank=True, max_length=30, null=True)),
                ('año', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('interpretacion', models.CharField(blank=True, choices=[('Ocupación', 'Ocupación'), ('Abandono', 'Abandono'), ('Construcción', 'Construcción'), ('Paleosuelo', 'Paleosuelo'), ('Reinstalación', 'Reinstalación'), ('Coluvión/Aluvión', 'Coluvión/Aluvión'), ('Destrucción', 'Destrucción'), ('Relleno', 'Relleno'), ('Otras', 'Otras')], max_length=16, null=True)),
                ('sector', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número de sector')),
                ('observaciones', models.TextField(blank=True, max_length=200, null=True)),
                ('latitud', models.FloatField(blank=True, null=True)),
                ('longitud', models.FloatField(blank=True, null=True)),
                ('cota_superior_diff', models.FloatField(blank=True, null=True, verbose_name='Cota superior (diferencia con punto cero)')),
                ('cota_inferior_diff', models.FloatField(blank=True, null=True, verbose_name='Cota inferior (diferencia con punto cero)')),
                ('pendiente_superior', models.CharField(blank=True, choices=[('Norte', 'Norte'), ('Sur', 'Sur'), ('Este', 'Este'), ('Oeste', 'Oeste'), ('Noroeste', 'Noroeste'), ('Noreste', 'Noreste'), ('Suroeste', 'Suroeste'), ('Sureste', 'Sureste')], max_length=8, null=True)),
                ('pendiente_inferior', models.CharField(blank=True, choices=[('Norte', 'Norte'), ('Sur', 'Sur'), ('Este', 'Este'), ('Oeste', 'Oeste'), ('Noroeste', 'Noroeste'), ('Noreste', 'Noreste'), ('Suroeste', 'Suroeste'), ('Sureste', 'Sureste')], max_length=8, null=True)),
                ('cota_superior', models.FloatField(blank=True, null=True)),
                ('cota_inferior', models.FloatField(blank=True, null=True)),
                ('bajo', models.ManyToManyField(blank=True, to='myFindings.ue')),
                ('equivalente_a', models.ManyToManyField(blank=True, to='myFindings.ue')),
                ('excavacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myFindings.excavation', to_field='n_excavacion')),
                ('hecho', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myFindings.fact')),
                ('igual_a', models.ManyToManyField(blank=True, to='myFindings.ue')),
                ('sobre', models.ManyToManyField(blank=True, to='myFindings.ue')),
            ],
        ),
        migrations.CreateModel(
            name='BuiltUE',
            fields=[
                ('ue_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myFindings.ue')),
                ('sistema_constructivo', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo', models.CharField(choices=[('Positiva', 'Positiva'), ('Negativa', 'Negativa')], default='Positiva', max_length=8)),
                ('n_estructura', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número de estructura')),
            ],
            options={
                'verbose_name': 'unidad construida',
                'verbose_name_plural': 'unidades construidas',
            },
            bases=('myFindings.ue',),
        ),
        migrations.CreateModel(
            name='SedimentaryUE',
            fields=[
                ('ue_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myFindings.ue')),
                ('tipo_estructura', models.CharField(blank=True, choices=[('Compacta', 'Compacta'), ('Suelta', 'Suelta'), ('Homogénea', 'Homogénea'), ('Heterogénea', 'Heterogénea')], max_length=15, null=True, verbose_name='Tipo de estructura')),
                ('tipo_textura', models.CharField(blank=True, choices=[('Arcilla', 'Arcilla'), ('Limo', 'Limo'), ('Arena', 'Arena'), ('Grava', 'Grava'), ('Cantos', 'Cantos'), ('Bloques', 'Bloques'), ('Cerámica', 'Cerámica'), ('Mortero', 'Mortero')], max_length=10, null=True, verbose_name='Tipo de textura')),
            ],
            options={
                'verbose_name': 'unidad sedimentaria',
                'verbose_name_plural': 'unidades sedimentarias',
            },
            bases=('myFindings.ue',),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(unique=True)),
                ('tipo', models.CharField(blank=True, max_length=50, null=True)),
                ('fase', models.CharField(blank=True, choices=[('A: época contemporánea', (('A1', 'A1: Siglo XVIII'), ('A2', 'A2: Siglo XIX'), ('A3', 'A3: Siglo XX'))), ('B: época moderna', (('B1', 'B1: Siglo XV'), ('B2', 'B2: Siglo XVI'), ('B3', 'B3: Siglo XVII'))), ('C: época medieval', (('C1', 'C1: fase emiral'), ('C2', 'C2: fase califal'), ('C3', 'C3: fase taifas'), ('C4', 'C4: fase almorávide/almohade'), ('C5', 'C5: fase nazarí'))), ('D: época romana', (('D1', 'D1: época republicana'), ('D2', 'D2: Alto Imperio'), ('D3', 'D3: Bajo Imperio'), ('D4', 'D4: Antigüedad tardía'))), ('E: época ibérica', (('E1', 'E1: Protoibérico-orientalizante'), ('E2', 'E2: Ibérico antiguo'), ('E3', 'E3: Ibérico pleno'), ('E4', 'E4: Ibérico tardío o final'))), ('F: Edad del Bronce', (('F1', 'F1: Bronce Antiguo'), ('F2', 'F2: Bronce Pleno'), ('F3', 'F3: Bronce Tardío'), ('F4', 'F4: Bronce Final')))], max_length=2, null=True)),
                ('vista_desde', models.CharField(blank=True, max_length=50, null=True)),
                ('dist_focal', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Distancia focal')),
                ('descripcion', models.TextField(blank=True, max_length=200, null=True)),
                ('imagen', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Imagen')),
                ('estancia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myFindings.room')),
                ('ue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myFindings.ue', verbose_name='UE (sedimentaria o construida)')),
            ],
            options={
                'verbose_name': 'fotografía',
                'verbose_name_plural': 'fotografías',
            },
        ),
        migrations.AddField(
            model_name='fact',
            name='estancia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myFindings.room', to_field='n_estancia'),
        ),
        migrations.AddConstraint(
            model_name='ue',
            constraint=models.UniqueConstraint(fields=('excavacion', 'n_orden'), name='ue_constraint'),
        ),
        migrations.AddField(
            model_name='sedimentaryue',
            name='materiales',
            field=models.ManyToManyField(blank=True, to='myFindings.sedimentarymaterial'),
        ),
        migrations.AddField(
            model_name='inclusion',
            name='uesedimentaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myFindings.sedimentaryue', verbose_name='UE sedimentaria'),
        ),
        migrations.AddConstraint(
            model_name='fact',
            constraint=models.UniqueConstraint(fields=('letra', 'numero'), name='fact_constraint'),
        ),
        migrations.AddField(
            model_name='builtue',
            name='materiales',
            field=models.ManyToManyField(blank=True, to='myFindings.builtmaterial'),
        ),
        migrations.AddConstraint(
            model_name='inclusion',
            constraint=models.UniqueConstraint(fields=('tipo', 'uesedimentaria'), name='inclusion_constraint'),
        ),
    ]
