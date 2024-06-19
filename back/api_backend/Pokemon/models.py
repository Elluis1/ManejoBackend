from django.db import models

# # Modelos para pokemons


class Pokemon(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField()
    
    class generations(models.TextChoices):
        GEN_1 = "GEN1", ("Generation I")
        GEN_2 = "GEN2", ("Generation II")
        GEN_3 = "GEN3", ("Generation III")
        GEN_4 = "GEN4", ("Generation IV")
        GEN_5 = "GEN5", ("Generation V")
        GEN_6 = "GEN6", ("Generation VI")
        GEN_7 = "GEN7", ("Generation VII")
        GEN_8 = "GEN8", ("Generation VIII")
    generation = models.CharField(
        max_length=4,
        choices=generations,
        blank=False
    )
    class types(models.TextChoices):
        NORMAL = "NOR", ("Normal")
        FIRE = "FIR", ("Fire")
        WATER = "WAT", ("Water")
        ELECTRIC = "ELE", ("Electric")
        GRASS = "GRA", ("Grass")
        ICE = "ICE", ("Ice")
        FIGHTING = "FIG", ("Fighting")
        POISON = "POI", ("Poison")
        GROUND = "GRO", ("Ground")
        FLYING = "FLY", ("Flying")
        PSYCHIC = "PSY", ("Psychic")
        BUG = "BUG", ("Bug")
        ROCK = "ROC", ("Rock")
        GHOST = "GHO", ("Ghost")
        DRAGON = "DRA", ("Dragon")
        DARK = "DAR", ("Dark")
        STEEL = "STE", ("Steel")
        FAIRY = "FAI", ("Fairy")
        
    type = models.CharField(
        max_length=4,
        choices=types,
        blank=False
    )
    subtype = models.CharField(
        max_length=4, 
        choices=types, 
        blank=True
    )

    def __str__(self) -> str:
        return self.name

class Trainer(models.Model):
    name = models.CharField(max_length=128)
    pokemons = models.ManyToManyField(Pokemon, blank=True)
    class regions(models.TextChoices):
        KANTO = "KAN", ("Kanto")
        JOHTO = "JOH", ("Johto")
        HOENN = "HOE", ("Hoenn")
        SINNOH = "SIN", ("Sinnoh")
        UNOVA = "UNO", ("Unova")
        KALOS = "KAL", ("Kalos")
        ALOLA = "ALO", ("Alola")
        GALAR = "GAL", ("Galar")
    region = models.CharField(max_length=3, choices=regions)

    def __str__(self) -> str:
        return self.name

#Terminado
