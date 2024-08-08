from django import forms
from .models import ContactView , FlightModel, CategoryFLightModel
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactView
        fields = '__all__'
        widgets={
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'placeholder': "Email"}),
            'phone': forms.TextInput(attrs={'placeholder': "Phone Number"}),
            'message': forms.Textarea(attrs={'placeholder': "Message"})

        }

class FlightForm(forms.ModelForm):

    class Meta:
        model = FlightModel
        fields = '__all__'
        widgets={
            'flying_from': forms.TextInput(attrs={'class': "form-control", 'type': "text", 'placeholder': "City or airport"}),
            'flying_to': forms.TextInput(attrs={'class': "form-control", 'type': "text", 'placeholder': "City or airport"}),
            'departing': forms.TextInput(attrs={'class': "form-control", 'type': "date"}),
            'returning': forms.TextInput(attrs={'class': "form-control", 'type': "date"}),
            'number_of_adults': forms.TextInput(attrs={'class': "form-control", 'type': "number"}),
            'number_of_children': forms.TextInput(attrs={'class': "form-control", 'type': "number"}),
            'travelClass': forms.Select(attrs={'class': "form-control"})
        }
