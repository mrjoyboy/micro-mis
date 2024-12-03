from django import forms
from .models import Event, Participant

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'end_date', 'event_type', 'province', 'district', 'municipality', 'ward_no', 'venue', 'latitude', 'longitude', 'partner_name']


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['event', 'first_name', 'last_name', 'ethnicity', 'occupation', 'email', 'phone_number', 'address']