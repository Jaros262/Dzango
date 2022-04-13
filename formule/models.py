from django.db import models

class Nationality(models.Model):
    nationality_name = models.CharField(max_length=20)
    nationality_shortcut = models.CharField(max_length=3)

class Team(models.Model):
    team_name = models.CharField(max_length=20)
    nationality_name = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name="Nationality")

class Racer(models.Model):
    racer_name = models.CharField(max_length=20)
    racer_surname = models.CharField(max_length=20)
    racer_rank = models.IntegerField(max_length=200)
    racer_formule_model = models.CharField(max_length=50)
    nationality_shortcut = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name="Nationality shortcut")
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Team name")
    #pub_date = models.DateTimeField('date published')

class Grand_prix(models.Model):
    nationality_name = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name="Nationality")
    grand_prix_lenght = models.IntegerField(max_length=30, help_text="Enter lenght in KM")
    grand_prix_max_racers = models.IntegerField(max_length=20)
    ENUM = (
        ("yes", "Yes"),
        ("no", "No"),
    )
    grand_prix_took_place = models.CharField(max_length=3, choices=ENUM)

class Sesion(models.Model):
    sesion_description = models.TextField(max_length=100)

