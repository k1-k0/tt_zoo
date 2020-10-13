from django.db import models


class Gender(models.TextChoices):
    MALE = 'M'
    FEMALE  = 'F'

class Animal(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.MALE)
    family = models.CharField(max_length=30)
    last_seen = models.TimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class AnimalType(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)


class Room(models.Model):
    class RoomType(models.TextChoices):
        CAGE = 'C'
        AVIARY = 'A'
        TERRARIUM = 'T'

    name = models.CharField(max_length=50)
    room_type = models.CharField(max_length=20, choices=RoomType.choices, default=RoomType.CAGE)
    area = models.PositiveIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)


class Zookeeper(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.MALE)
    hire_date = models.DateTimeField()
    salary = models.DecimalField(max_digits=10, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    animals = models.ManyToManyField(Animal)