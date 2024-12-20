from django.contrib import admin
from .models import EventType, Province, District, Municipality, Ethnicity, Occupation, Project, Event, Participant, Title, MunicipalityType, Gender, CertifiedStatus, ProjectFile

admin.site.register(EventType)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Municipality)
admin.site.register(Ethnicity)
admin.site.register(Occupation)
admin.site.register(Project)
admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(Title)
admin.site.register(MunicipalityType)
admin.site.register(Gender)
admin.site.register(CertifiedStatus)

@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'uploaded_at']
    list_filter = ['project']







