from django import forms
from .models import Message

LOCATIONS = (
    ('', 'Choose...'),
    ("Migori", "Migori"), 
    ("Homabay", "Homabay"), 
    ("Kisii", "Kisii"), 
    ("Awendo", "Awendo")
)

REASONS = (
    ('', 'Choose...'),
    ("Depression", "Depression"), 
    ("Sexual Abuse", "Sexual Abuse"), 
    ("Gender Based Violence", "Gender Based Violence"), 
    ("Substance Abuse", "Substance Abuse")
)

class AddressForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'firstname', 'lastname', 'email', 'id_number', 'phone_number', 'location', 'reason', 'message'
        ]
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Firstname'}), required=True)
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Lastname'}), required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), required=True)
    id_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'ID Number'}),required=True)
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Telephone'}),required=True)
    location = forms.ChoiceField(choices=LOCATIONS, required=True)
    reason = forms.ChoiceField(choices=REASONS, required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message'}))