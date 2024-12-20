from django.db import models
from django.utils import timezone


# Event Type Model
class EventType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Province Model
class Province(models.Model):
    name = models.CharField(max_length=100)
    area_sq_km = models.FloatField()
    website = models.CharField(max_length=255)
    headquarter = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# District Model
class District(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    area_sq_km = models.FloatField()
    website = models.CharField(max_length=255)
    headquarter = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Municipality Model

class MunicipalityType(models.Model):
    name = models.CharField(max_length=100)
    short_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Municipality(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    municipality_type = models.ForeignKey(MunicipalityType, on_delete=models.CASCADE)
    area_sq_km = models.FloatField()
    website = models.CharField(max_length=255)
    no_of_wards = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Municipalities"

class Title(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

# Ethnicity Model
class Ethnicity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Ethnicities"

# Occupation Model
class Occupation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class CertifiedStatus(models.Model):
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
    
class ProjectFile(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, related_name='project_files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='project_files/')
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# Event Model
class Event(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
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
    organizing_partners = models.CharField(max_length=255)
    funding_partners = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    ethnicity = models.ForeignKey(Ethnicity, on_delete=models.CASCADE)
    disability = models.BooleanField(default=False)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    organization = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True, db_column='organization_designation')
    certification = models.ForeignKey(CertifiedStatus, on_delete=models.CASCADE)
    # certification = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    



