Structure de la base de données et modèles
==========================================

Vue d'ensemble
---------------

L'application utilise SQlite comme système de gestion de base de données.
La Structure est définie par les modèles Django qui sont automatiquements convertis en table SQL via l'ORM de Django


Modèles de données 
-------------------

l'application comprend trois modèles principaux répartis dans deux applications Django :

Application Lettings:
~~~~~~~~~~~~~~~~~~~~~

**Modèle Address**

- Représente les adresse des biens immobiliers :

   .. code-block:: python

      class Address(models.Model):
         number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
         street = models.CharField(max_length=64)
         city = models.CharField(max_length=64)
         state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
         zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
         country_iso_code = models.CharField(
            max_length=3, validators=[MinLengthValidator(3)]
         )

Attributs:\n

- ``number`` : numéro de l'adresse (entier limité à 9999)\n
- ``street`` : nom de la rue (limité à 64 caractères)\n
- ``city`` : la ville (limité à 64 caractères)\n
- ``state`` : l'état (2 caratères)\n
- ``zip_code`` : le code postal (entier limité à 99999)\n
- ``country_iso_code`` : le code ISO du pays (3 caractères)


**Modèles Lettings**

- Représente les locations des biens immobiliers :
   
   .. code-block:: python

      class Letting(models.Model):
         title = models.CharField(max_length=256)
         address = models.OneToOneField(Address, on_delete=models.CASCADE)

Attributs:

- ``title`` : titre de la location (limité à 256 caractères)\n
- ``address`` : Relation OneToOne avec le modèle ``Address`` (suppression en cascade)\n


Application Profiles
~~~~~~~~~~~~~~~~~~~~~

**Modèle Profiles**

Représente les profils des utilisateurs :

.. code-block:: python

   class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      favorite_city = models.CharField(max_length=64, blank=True)

Attributs:\n
- ``user`` : Relation OneToOne avec le modèle ``User`` (suppression en cascade)\n
- ``favorite_city`` : la ville préférée (limité à 64 caractères)\n

Modèle User (Django)
--------------------

Le modèle User est fourni par Django et est utilisé pôur l'authentification et l'autorisation.


Contraintes d'intégrité
---------------------

- Les adresses ne peuvent pas être partagées entre plusieurs locations (relation OneToOne)
- Un utilisateur ne peut avoir qu'un seul profil (relation OneToOne)
- Si une adresse est supprimée, la location associée l'est également (suppression en cascade)
- Si un utilisateur est supprimé, son profil l'est également (suppression en cascade)
