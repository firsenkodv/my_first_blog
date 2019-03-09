from django import forms

class SendingForm(forms.Form):
     name=forms.CharField(label="Enter your name", max_length=100)
     email=forms.EmailField(label="Enter email", max_length=100)
