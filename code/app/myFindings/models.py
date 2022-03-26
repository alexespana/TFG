from django.db import models

FASE_CHOICES = [
    (('A: época contemporánea'), (
            ('A1','A1: 1800/1900'),
            ('A2','A2: 1900/2000'),
            ('A3','A3: época actual'),
        )
    ),
    (('B: época moderna'),(
            ('B1','B1: fase morisca'),
            ('B2','B2: fase cristiana'),
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
            ('E1','E1: Protoibérico'),
            ('E2','E2: Ibérico antiguo'),
            ('E3','E3: Ibérico pleno'),
            ('E4','E4: Ibérico tardío o final'),
        )
    ),
    (('F: Edad del Bronce'), (
            ('F1','F1: Bronce Final'),
            ('F2','F2: Bronce argárico'),
            ('F3','F3: Bronce antiguo'),
        )
    ),
]

PERIODO_CHOICES = [
    ('Contemporánea: 1800/1900','Contemporánea: 1800/1900'),
    ('Contemporánea: 1900/2000','Contemporánea: 1900/2000'),
    ('Contemporánea: actualidad','Contemporánea: actualidad'),
    ('Moderna: morisca','Moderna: morisca'),
    ('Moderna: cristiana','Moderna: cristiana'),
    ('Medieval: emiral','Medieval: emiral'),
    ('Medieval: califal','Medieval: califal'),
    ('Medieval: taifas','Medieval: taifas'),
    ('Medieval: almorávide/almohade','Medieval: almorávide/almohade'),
    ('Medieval: nazarí','Medieval: nazarí'),
    ('Romana: época republicana','Romana: época republicana'),
    ('Romana: Alto Imperio','Romana: Alto Imperio'),
    ('Romana: Bajo Imperio','Romana: Bajo Imperio'),
    ('Romana: Antigüedad tardía','Romana: Antigüedad tardía'),
    ('Ibérica: Protoibérico','Ibérica: Protoibérico'),
    ('Ibérica: Ibérico antiguo','Ibérica: Ibérico antiguo'),
    ('Ibérica: Ibérico pleno','Ibérica: Ibérico pleno'),
    ('Ibérica: Ibérico tardío o final','Ibérica: Ibérico tardío o final'),
    ('Edad del Bronce: final','Edad del Bronce: final'),
    ('Edad del Bronce: argárico','Edad del Bronce: argárico'),
    ('Edad del Bronce: antiguo','Edad del Bronce: antiguo'),
]


# Create your models here.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ESTANCIA            ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Estancia(models.Model):
    n_estancia = models.CharField(max_length=5, unique=True)     # ES001, ES002, etc
    n_zona = models.PositiveSmallIntegerField()
    n_sector = models.PositiveSmallIntegerField()
    observaciones = models.CharField(max_length=200)
    croquis_planta = models.ImageField()
    n_planta = models.PositiveSmallIntegerField()
    n_seccion = models.PositiveSmallIntegerField()
    elevacion = models.PositiveSmallIntegerField()
    tpq = models.PositiveSmallIntegerField()
    taq = models.PositiveSmallIntegerField()
    fase = models.CharField(max_length=2, choices=FASE_CHOICES)
    periodo = models.CharField(max_length=100, choices=PERIODO_CHOICES)
    autor = models.CharField(max_length=50)

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
    estancia = models.ForeignKey(Estancia, on_delete=models.CASCADE)

    # Unique key
    letra = models.CharField(max_length=2, choices=LETRA_CHOICES)
    numero = models.CharField(max_length=6)    # Number of stratigrafic unit that identifies the fact

    fase = models.CharField(max_length=2, choices=FASE_CHOICES)
    tpq = models.PositiveSmallIntegerField()
    taq = models.PositiveSmallIntegerField()
    definicion = models.CharField(max_length=100)
    comentarios = models.CharField(max_length=100)
    sector = models.PositiveSmallIntegerField()
    zona = models.PositiveSmallIntegerField()
    año = models.PositiveSmallIntegerField()
    estructura = models.PositiveSmallIntegerField() 
    croquis_plan = models.ImageField()
    croquis_seccion = models.ImageField()

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
    latitud = models.FloatField()
    longitud = models.FloatField()
    altura = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.n_excavacion)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# UE                  ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UE(models.Model):
    INTERPRETACION_CHOICES = [
        ('Ocupacion','Ocupación'),
        ('Abandono','Abandono'),
        ('Contruccion','Construcción'),
        ('Paleosuelo','Paleosuelo'),
        ('Reinstalacion','Reinstalación'),
        ('Coluvion','Coluvión/Aluvión'),
        ('Destruccion','Destrucción'),
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
    excavacion = models.ForeignKey(Excavacion, on_delete=models.CASCADE)

    plano_n = models.PositiveSmallIntegerField()
    seccion_n = models.PositiveSmallIntegerField()
    elevacion_n = models.PositiveSmallIntegerField()
    croquis_planta = models.ImageField()
    croquis_seccion = models.ImageField()
    tpq = models.PositiveSmallIntegerField()
    taq = models.PositiveSmallIntegerField()
    fase = models.CharField(max_length=2, choices=FASE_CHOICES)
    periodo = models.CharField(max_length=100, choices=PERIODO_CHOICES)
    descripcion = models.TextField(max_length=200)
    autor = models.CharField(max_length=30)
    año = models.PositiveSmallIntegerField()
    interpretacion = models.CharField(max_length=13, choices=INTERPRETACION_CHOICES)    
    sector = models.PositiveSmallIntegerField()          
    observaciones = models.TextField(max_length=200)
    latitud = models.FloatField()
    longitud = models.FloatField()


    cota_superior_diff = models.IntegerField()
    cota_inferior_diff = models.IntegerField()

    pendiente_superior = models.CharField(max_length=8, choices=PENDIENTE_CHOICES)
    pendiente_inferior = models.CharField(max_length=8, choices=PENDIENTE_CHOICES)

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
    # Foreign Keys
    ue = models.ForeignKey(UE, on_delete=models.CASCADE)
    estancia = models.ForeignKey(Estancia, on_delete=models.CASCADE)

    numero = models.PositiveIntegerField(unique=True)
    tipo = models.CharField(max_length=50)
    fase = models.CharField(max_length=2, choices=FASE_CHOICES)
    vista_desde = models.CharField(max_length=50)
    dist_focal = models.PositiveSmallIntegerField()
    descripcion = models.TextField(max_length=200)
    imagen = models.ImageField()

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

    nombre = models.CharField(max_length=20, choices=NOMBRE_CHOICES, primary_key=True)

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

    tipo_estructura = models.CharField(max_length=15, choices=ESTRUCTURA_CHOICES)
    tipo_textura = models.CharField(max_length=10, choices=TEXTURA_CHOICES)
    materiales_sedimentarios = models.ManyToManyField(MaterialSedimentaria)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# UECONSTRUIDA        ~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UEConstruida(UE):
    TIPO_CHOICES = [
        ('POS', 'Positiva'),
        ('NEG', 'Negativa'),
    ]

    sistema_constructivo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=3, choices=TIPO_CHOICES)
    materiales_construidos = models.ManyToManyField(MaterialConstruida)
    n_estructura = models.PositiveSmallIntegerField(default=0)

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

    frecuencia = models.CharField(max_length=10, choices=FRECUENCIA_CHOICES)
    grosor = models.CharField(max_length=10, choices=GROSOR_CHOICES)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tipo', 'uesedimentaria'], name='inclusion_constraint')                                                  
        ]

    def __str__(self):
        return self.tipo
