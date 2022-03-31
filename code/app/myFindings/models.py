from django.db import models

FASE_CHOICES = [
    (('A: época contemporánea'), (
            ('A1','A1: Siglo XVIII'),
            ('A2','A2: Siglo XIX'),
            ('A3','A3: Siglo XX'),
        )
    ),
    (('B: época moderna'),(
            ('B1','B1: Siglo XV'),
            ('B2','B2: Siglo XVI'),
            ('B3','B3: Siglo XVII'),
        )
    ),
    (('C: época medieval'), (
            ('C1','C1: fase emiral'),
            ('C2','C2: fase califal'),
            ('C3','C3: fase taifas'),
            ('C4','C4: fase almorávide/almohade'),
            ('C5','C5: fase nazarí'),
        )
    ),
    (('D: época romana'), (
            ('D1','D1: época republicana'),
            ('D2','D2: Alto Imperio'),
            ('D3','D3: Bajo Imperio'),
            ('D4','D4: Antigüedad tardía'),
        )
    ),
    (('E: época ibérica'), (
            ('E1','E1: Protoibérico-orientalizante'),
            ('E2','E2: Ibérico antiguo'),
            ('E3','E3: Ibérico pleno'),
            ('E4','E4: Ibérico tardío o final'),
        )
    ),
    (('F: Edad del Bronce'), (
            ('F1','F1: Bronce Antiguo'),
            ('F2','F2: Bronce Pleno'),
            ('F3','F3: Bronce Tardío'),
            ('F4','F4: Bronce Final'),
        )
    ),
]

PERIODO_CHOICES = [
    ('Siglo XVIII','Contemporánea: Siglo XVIII'),
    ('Siglo XIX','Contemporánea: Siglo XIX'),
    ('Siglo XX','Contemporánea: Siglo XX'),
    ('Siglo XV','Moderna: Siglo XV'),
    ('Siglo XVI','Moderna: Siglo XVI'),
    ('Siglo XVII','Moderna: Siglo XVII'),
    ('Fase emiral','Medieval: emiral'),
    ('Fase califal','Medieval: califal'),
    ('Fase taifas','Medieval: taifas'),
    ('Fase invasiones almorávides y almohades','Medieval: almorávide/almohade'),
    ('Fase nazarí','Medieval: nazarí'),
    ('Fase republicana','Romana: época republicana'),
    ('Fase Altoimperial','Romana: Alto Imperio'),
    ('Fase Bajoimperial','Romana: Bajo Imperio'),
    ('Antigüedad tardía','Romana: Antigüedad tardía'),
    ('Protoibérico-orientalizante','Ibérica: Protoibérico'),
    ('Ibérico antiguo','Ibérica: Ibérico antiguo'),
    ('Ibérico pleno','Ibérica: Ibérico pleno'),
    ('Ibérico final','Ibérica: Ibérico tardío o final'),
    ('Bronce antiguo','Edad del Bronce: Antiguo'),
    ('Bronce pleno','Edad del Bronce: Pleno'),
    ('Bronce tardío','Edad del Bronce: Tardío'),
    ('Bronce final','Edad del Bronce: Final'),
]


# Create your models here.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ESTANCIA            ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Estancia(models.Model):
    n_estancia = models.CharField(max_length=5, unique=True)     # ES001, ES002, etc
    n_zona = models.PositiveSmallIntegerField(blank=True, null=True)
    n_sector = models.PositiveSmallIntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    croquis_planta = models.ImageField(blank=True, null=True)
    n_planta = models.PositiveSmallIntegerField(blank=True, null=True)
    n_seccion = models.PositiveSmallIntegerField(blank=True, null=True)
    elevacion = models.PositiveSmallIntegerField(blank=True, null=True)
    tpq = models.PositiveSmallIntegerField(blank=True, null=True)
    taq = models.PositiveSmallIntegerField(blank=True, null=True)
    fase = models.CharField(max_length=2, choices=FASE_CHOICES, blank=True, null=True)
    periodo = models.CharField(max_length=100, choices=PERIODO_CHOICES, blank=True, null=True)
    autor = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.n_estancia

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HECHO               ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Hecho(models.Model):
    LETRA_CHOICES = [
        ('MR','Muro'),
        ('SL','Suelo'),
        ('PO','Pozo'),
        ('FS','Fosa'),
        ('SI','Silo'),
        ('PR','Puerta'),
        ('CN','Canalización'),
        ('DP','Depósito'),
        ('TN','Tinaja'),
        ('ES','Sin identificación'),
    ]

    # Foreign keys
    estancia = models.ForeignKey(Estancia, on_delete=models.CASCADE, blank=True, null=True)

    # Unique key
    letra = models.CharField(max_length=2, choices=LETRA_CHOICES)
    numero = models.CharField(max_length=6)    # Number of stratigrafic unit that identifies the fact

    fase = models.CharField(max_length=2, choices=FASE_CHOICES, blank=True, null=True)
    tpq = models.PositiveSmallIntegerField(blank=True, null=True)
    taq = models.PositiveSmallIntegerField(blank=True, null=True)
    definicion = models.CharField(max_length=100, blank=True, null=True)
    comentarios = models.CharField(max_length=100, blank=True, null=True)
    sector = models.PositiveSmallIntegerField(blank=True, null=True)
    zona = models.PositiveSmallIntegerField(blank=True, null=True)
    año = models.PositiveSmallIntegerField(blank=True, null=True)
    estructura = models.PositiveSmallIntegerField(blank=True, null=True) 
    croquis_plan = models.ImageField(blank=True, null=True)
    croquis_seccion = models.ImageField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['letra', 'numero'], name='fact_constraint')                                                  
        ]

    def __str__(self):
        return self.letra + self.numero

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EXCAVACION          ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Excavacion(models.Model):
    n_excavacion = models.PositiveIntegerField(unique=True, verbose_name='Número de excavación')
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    altura = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.n_excavacion)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# UE                  ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UE(models.Model):
    INTERPRETACION_CHOICES = [
        ('Ocupación','Ocupación'),
        ('Abandono','Abandono'),
        ('Contrucción','Construcción'),
        ('Paleosuelo','Paleosuelo'),
        ('Reinstalación','Reinstalación'),
        ('Coluvión/Aluvión','Coluvión/Aluvión'),
        ('Destrucción','Destrucción'),
        ('Relleno','Relleno'),
        ('Otras','Otras'),
    ]

    PENDIENTE_CHOICES = [
        ('Norte','Norte'),
        ('Sur','Sur'),
        ('Este','Este'),
        ('Oeste','Oeste'),
        ('Noroeste','Noroeste'),
        ('Noreste','Noreste'),
        ('Suroeste','Suroeste'),
        ('Sureste','Sureste'),
    ]

    codigo = models.CharField(unique=True, max_length=6, default='000000')
    # Foreign Keys
    hecho = models.ForeignKey(Hecho, on_delete=models.CASCADE, blank=True, null=True)
    excavacion = models.ForeignKey(Excavacion, on_delete=models.CASCADE, to_field='n_excavacion')

    plano_n = models.PositiveSmallIntegerField(blank=True, null=True)
    seccion_n = models.PositiveSmallIntegerField(blank=True, null=True)
    elevacion_n = models.PositiveSmallIntegerField(blank=True, null=True)
    croquis_planta = models.ImageField(blank=True, null=True)
    croquis_seccion = models.ImageField(blank=True, null=True)
    tpq = models.PositiveSmallIntegerField(blank=True, null=True)
    taq = models.PositiveSmallIntegerField(blank=True, null=True)
    fase = models.CharField(max_length=2, choices=FASE_CHOICES, blank=True, null=True)
    periodo = models.CharField(max_length=100, choices=PERIODO_CHOICES, blank=True, null=True)
    descripcion = models.TextField(max_length=200, blank=True, null=True)
    autor = models.CharField(max_length=30, blank=True, null=True)
    año = models.PositiveSmallIntegerField(blank=True, null=True)
    interpretacion = models.CharField(max_length=16, choices=INTERPRETACION_CHOICES, blank=True, null=True)    
    sector = models.PositiveSmallIntegerField(blank=True, null=True)          
    observaciones = models.TextField(max_length=200, blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)


    cota_superior_diff = models.SmallIntegerField(blank=True, null=True)
    cota_inferior_diff = models.SmallIntegerField(blank=True, null=True)

    pendiente_superior = models.CharField(max_length=8, choices=PENDIENTE_CHOICES, blank=True, null=True)
    pendiente_inferior = models.CharField(max_length=8, choices=PENDIENTE_CHOICES,  blank=True, null=True)

    def _get_cota_superior(self):
        return self.excavacion.altura + self.cota_superior_diff

    def _get_cota_inferior(self):
        return self.excavacion.altura + self.cota_inferior_diff

    # Calculated fields 
    cota_superior = property(_get_cota_superior)
    cota_inferior = property(_get_cota_inferior)

    def __str__(self):
        return str(self.descripcion)

class Fotografia(models.Model):
    numero = models.PositiveIntegerField(unique=True)
   
    # Foreign Keys
    ue = models.ForeignKey(UE, on_delete=models.CASCADE, blank=True, null=True)
    estancia = models.ForeignKey(Estancia, on_delete=models.CASCADE, blank=True, null=True)

    tipo = models.CharField(max_length=50, blank=True, null=True)
    fase = models.CharField(max_length=2, choices=FASE_CHOICES, blank=True, null=True)
    vista_desde = models.CharField(max_length=50, blank=True, null=True)
    dist_focal = models.PositiveSmallIntegerField(blank=True, null=True)
    descripcion = models.TextField(max_length=200, blank=True, null=True)
    imagen = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.numero

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MATERIALSEDIMENTARIA ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MaterialSedimentaria(models.Model):
    NOMBRE_CHOICES = [
        ('Muestras', 'Muestras'),
        ('Metal', 'Metal'),
        ('Piedra', 'Piedra'),
        ('Arcilla', 'Arcilla'),
        ('Material construido', 'Material construido'),
        ('Cerámica', 'Cerámica'),
        ('Vidrio', 'Vidrio'),
        ('Fauna', 'Fauna'),
        ('Otros', 'Otros'),
    ]

    nombre = models.CharField(max_length=21, choices=NOMBRE_CHOICES, primary_key=True)

    def __str__(self):
        return self.nombre

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MATERIALCONSTRUIDA   ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MaterialConstruida(models.Model):
    NOMBRE_CHOICES = [
        ('Piedra', 'Piedra'),
        ('Tierra cruda', 'Tierra cruda'),
        ('Cal', 'Cal'),
        ('Tierra cocida', 'Tierra cocida'),
        ('Madera', 'Madera'),
    ]

    nombre = models.CharField(max_length=15, choices=NOMBRE_CHOICES, primary_key=True)

    def __str__(self):
        return self.nombre

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# UESEDIMENTARIA      ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UESedimentaria(UE):
    ESTRUCTURA_CHOICES = [
        ('Compacta', 'Compacta'),
        ('Suelta', 'Suelta'),
        ('Homogénea', 'Homogénea'),
        ('Heterogénea', 'Heterogénea'),
    ]

    TEXTURA_CHOICES = [
        ('Arcilla','Arcilla'),
        ('Limo','Limo'),
        ('Arena','Arena'),
        ('Grava','Grava'),
        ('Cantos','Cantos'),
        ('Bloques','Bloques'),
        ('Cerámica','Cerámica'),
        ('Mortero','Mortero'),
    ]

    tipo_estructura = models.CharField(max_length=15, choices=ESTRUCTURA_CHOICES, blank=True, null=True)
    tipo_textura = models.CharField(max_length=10, choices=TEXTURA_CHOICES, blank=True, null=True)
    materiales = models.ManyToManyField(MaterialSedimentaria, blank=True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# UECONSTRUIDA        ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UEConstruida(UE):
    TIPO_CHOICES = [
        ('Positiva', 'Positiva'),
        ('Negativa', 'Negativa'),
    ]

    sistema_constructivo = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=8, choices=TIPO_CHOICES, blank=True, null=True)
    materiales = models.ManyToManyField(MaterialConstruida, blank=True)
    n_estructura = models.PositiveSmallIntegerField(default=0, blank=True, null=True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# INCLUSION           ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Inclusion(models.Model):
    FRECUENCIA_CHOICES = [
        ('Ausencia', 'Ausencia'),
        ('Ocasional', 'Ocasional'),
        ('Medio', 'Medio'),
        ('Frecuente', 'Frecuente'),
    ]

    GROSOR_CHOICES = [
        ('< 2 cm', '< 2 cm'),
        ('2-6 cm', '2-6 cm'),
        ('6-12 cm', '6-12 cm'),
        ('> 12 cm', '> 12 cm'),
    ]

    TIPO_CHOICES = [
        ('Cenizas', 'Cenizas'),
        ('Carbones', 'Carbones'),
        ('Huesos', 'Huesos'),
        ('Adobe', 'Adobe'),
        ('Cañizo', 'Cañizo'),
        ('Tejas', 'Tejas'),
        ('Bloques', 'Bloques'),
        ('Cal', 'Cal'),
        ('Mortero', 'Mortero'),
        ('Enlucido', 'Enlucido'),
    ]
    
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    # Foreign Keys
    uesedimentaria = models.ForeignKey(UESedimentaria, on_delete=models.CASCADE)

    frecuencia = models.CharField(max_length=10, choices=FRECUENCIA_CHOICES, blank=True, null=True)
    grosor = models.CharField(max_length=10, choices=GROSOR_CHOICES, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tipo', 'uesedimentaria'], name='inclusion_constraint')                                                  
        ]

    def __str__(self):
        return self.tipo
