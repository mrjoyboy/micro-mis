from django import forms
from .models import Event, Participant, Project, EventType, Province, District, Municipality, ProjectFile

class EventForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'end_date', 'event_type', 'province', 'district', 'municipality', 'ward_no', 'venue', 'latitude', 'longitude', 'organizing_partners', 'funding_partners']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ParticipantForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Participant
        fields = ['title', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'gender', 'ethnicity', 'disability', 'occupation', 'organization', 'designation', 'certification']


class ProjectForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ProjectFileForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields = ['name', 'file']

class EventTypeForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = EventType
        fields = ['name', 'description']