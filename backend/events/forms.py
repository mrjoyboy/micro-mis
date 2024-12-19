from django import forms
from .models import Event, Participant, Project, EventType, Province, District, Municipality

class EventForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Event
        fields = ['name', 'project', 'start_date', 'end_date', 'event_type', 'province', 'district', 'municipality', 'ward_no', 'venue', 'latitude', 'longitude', 'organizing_partners', 'funding_partners']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }



    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['province'].queryset = Province.objects.all()
    #     self.fields['district'].queryset = District.objects.none()
    #     self.fields['municipality'].queryset = Municipality.objects.none()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     # Add asterisk to required fields
    #     for field_name, field in self.fields.items():
    #         if field.required:
    #             field.label = f"{field.label} *"

    #     # Province field setup
    #     self.fields['province'].queryset = Province.objects.all().order_by('name')
    #     self.fields['province'].widget.attrs.update({'class': 'form-select'})

    #     # District field setup
    #     self.fields['district'].queryset = District.objects.none()
    #     self.fields['district'].widget.attrs.update({'class': 'form-select'})

    #     # Municipality field setup
    #     self.fields['municipality'].queryset = Municipality.objects.none()
    #     self.fields['municipality'].widget.attrs.update({'class': 'form-select'})

    #     # Prefill district and municipality if an instance is being edited
    #     if self.instance.pk:
    #         if self.instance.province:
    #             self.fields['district'].queryset = District.objects.filter(province=self.instance.province).order_by('name')
    #         if self.instance.district:
    #             self.fields['municipality'].queryset = Municipality.objects.filter(district=self.instance.district).order_by('name')


class ParticipantForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Participant
        fields = ['event', 'title', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'gender', 'ethnicity', 'disability', 'occupation', 'organization', 'designation', 'certification']


class ProjectForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class EventTypeForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = EventType
        fields = ['name', 'description']