from django import forms

class StudentForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=4)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea())
    
