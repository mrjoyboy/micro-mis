from django.db import models

# Create your models here.
from django.db import models

# Event Type Model
class EventType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Province Model
class Province(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# District Model
class District(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Municipality Model
class Municipality(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    no_of_wards = models.IntegerField()

    def __str__(self):
        return self.name

# Ethnicity Model
class Ethnicity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Occupation Model
class Occupation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Project Model
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

# Event Model
class Event(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    event_type = models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    ward_no = models.IntegerField()
    venue = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    partner_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Participant(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ethnicity = models.ForeignKey('Ethnicity', on_delete=models.SET_NULL, null=True, blank=True)
    occupation = models.ForeignKey('Occupation', on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"