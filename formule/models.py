from django.db import models

class Nationality(models.Model):
    nationality_name = models.CharField(max_length=20, verbose_name='Name')
    nationality_shortcut = models.CharField(max_length=3, verbose_name='Shortcut')

    class Meta:
        ordering = ['nationality_name']

    def __str__(self):
        return self.nationality_name

class Team(models.Model):
    team_name = models.CharField(max_length=20, verbose_name='Name')
    nationality_name = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name="Nationality")

    class Meta:
        ordering = ['team_name']

    def __str__(self):
        return self.team_name

class Racer(models.Model):
    racer_name = models.CharField(max_length=20, verbose_name='Name')
    racer_surname = models.CharField(max_length=20, verbose_name='Surname')
    racer_rank = models.IntegerField(verbose_name='Rank')
    racer_formule_model = models.CharField(max_length=50, verbose_name='Formule model')
    nationality_shortcut = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name="Nationality shortcut")
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Team name")
    racer_born = models.DateField(verbose_name='Born date')

    class Meta:
        ordering = ['racer_name']

    def __str__(self):
        return self.racer_name

class Grand_prix(models.Model):
    track_name = models.CharField(max_length=20, verbose_name='Track name')
    nationality_name = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name="Nationality")
    grand_prix_lenght = models.DecimalField(default=3100,max_digits=6, decimal_places=2, help_text="Enter lenght in Km", verbose_name='Track lenght')
    grand_prix_max_racers = models.IntegerField(verbose_name='Max. Racers')
    ENUM = (
        ("yes", "Yes"),
        ("no", "No"),
    )
    grand_prix_took_place = models.CharField(max_length=3, choices=ENUM, verbose_name='Took place')

    class Meta:
        ordering = ['track_name']

    def __str__(self):
        return self.track_name

class Sesion(models.Model):
    sesion_year = models.IntegerField(default=1950, verbose_name="Year")
    sesion_description = models.TextField(max_length=750, verbose_name='Description')

    class Meta:
        ordering = ['sesion_year']
    def __str__(self):
        return f'{self.sesion_year}'