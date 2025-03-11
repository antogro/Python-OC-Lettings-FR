from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Représente une adresse avec des contraintes sur les champs."""
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    class Meta:
        """
        Permet de définir des options pour le modèle.
        verbose_name_plural = "Adresses" permet de définir le nom du modèle au pluriel.
        """
        verbose_name_plural = "Adresses"

    def __str__(self):
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """Représente une location liée à une adresse."""
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
