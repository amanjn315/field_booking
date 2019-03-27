from django import forms
from .models import Field_Book



class NewFieldForm(forms.ModelForm):
    class Meta:
        model = Field_Book
        fields = '__all__'
        labels = {
            "name": "Full Name: ",
            "roll": "Roll Number: ",
            "Mobile_number": "Mobile Number: ",
            "email": "Email: ",
            "field": "Field Name: ",
            "date": "Date of Booking: ",
            "ftime": 'From Time: ',
            "ttime": "To Time: ",
            "purpose": "Enter your purpose of booking: "
        }
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'user@gmail.com'}),
            'date': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'ftime': forms.TextInput(attrs={'placeholder': 'HH:MM:SS'}),
            'ttime': forms.TextInput(attrs={'placeholder': 'HH:MM:SS'}),
        }
