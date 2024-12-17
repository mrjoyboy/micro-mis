from django import forms
from .models import Event, Participant, Project, EventType

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'project', 'start_date', 'end_date', 'event_type', 'province', 'district', 'municipality', 'ward_no', 'venue', 'latitude', 'longitude', 'organizing_partners', 'funding_partners']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['event', 'title', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'gender', 'ethnicity', 'disability', 'occupation', 'organization', 'organization_designation', 'certification']
        widgets = {
            'disability': forms.CheckboxInput(),
            'certification': forms.CheckboxInput(),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class EventTypeForm(forms.ModelForm):
    class Meta:
        model = EventType
        fields = ['name', 'description']