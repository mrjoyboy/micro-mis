from django.contrib import admin
from .models import EventType, Province, District, Municipality, Ethnicity, Occupation, Project, Event

admin.site.register(EventType)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Municipality)
admin.site.register(Ethnicity)
admin.site.register(Occupation)
admin.site.register(Project)
admin.site.register(Event)
