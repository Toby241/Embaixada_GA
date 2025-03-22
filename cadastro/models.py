from django.db import models

class Cadastro(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    date_naissance = models.DateField(verbose_name="Date de naissance")
    passport = models.CharField(max_length=50, verbose_name="Passport")
    rnm = models.CharField(max_length=50, verbose_name="RNM")
    adresse = models.TextField(verbose_name="Adresse complète")
    ville = models.CharField(max_length=100, verbose_name="Ville")
    etat = models.CharField(max_length=100, verbose_name="État")
    contact = models.CharField(max_length=20, verbose_name="Contact")
    email = models.EmailField(verbose_name="E-mail")
    etudiant = models.CharField(max_length=3, choices=[('sim', 'Oui'), ('nao', 'Non')], verbose_name="Vous êtes étudiant ?")
    cours = models.CharField(max_length=200, blank=True, null=True, verbose_name="Cours")
    etablissement = models.CharField(max_length=200, blank=True, null=True, verbose_name="Établissement")
    profession = models.CharField(max_length=200, blank=True, null=True, verbose_name="Profession")

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    class Meta:
        verbose_name = "Cadastro"
        verbose_name_plural = "Cadastros"