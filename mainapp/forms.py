from django import forms
from .models import Center


class CenterForm(forms.ModelForm):
    class Meta:
        model = Center
        fields = [
            'name_of_center',
            'po_box',
            'telephone',
            'contact_person',
            'email',
            'physical_location'
        ]
        widgets = {
            'name_of_center': forms.TextInput(attrs={"class":"form-control", "rows": 1, "cols": 20}),
            'po_box': forms.TextInput(attrs={"class":"form-control", "rows": 1, "cols": 20}),
            'telephone': forms.TextInput(attrs={"class":"form-control", "rows": 1, "cols": 20}),
            'contact_person': forms.TextInput(attrs={"class":"form-control", "rows": 1, "cols": 20}),
            'email': forms.TextInput(attrs={"class":"form-control", "rows": 1, "cols": 20}),
            'physical_location': forms.TextInput(attrs={"class":"form-control", "rows": 1, "cols": 20}),
        }



class EditCenterForm(forms.ModelForm):
    class Meta:
        model = Center
        fields = ['name_of_center', 'telephone', 'contact_person', 'email']
        widgets = {
            'name_of_center': forms.TextInput(attrs={"class":"form-control", "rows": 1, "cols": 20}),
            'telephone': forms.TextInput(attrs={"class":"form-control", "rows": 1, "cols": 20}),
            'contact_person': forms.TextInput(attrs={"class":"form-control", "rows": 1, "cols": 20}),
            'email': forms.TextInput(attrs={"class":"form-control", "rows": 1, "cols": 20}),
        } 

