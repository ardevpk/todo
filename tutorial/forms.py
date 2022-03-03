from django import forms

class UserForm(forms.Form):
    num1 = forms.CharField(label="First Name", widget=forms.TextInput(attrs={
        "placeholder":"First Value Input",
        "class":"form-control"
    }))
    num2 = forms.CharField(label="Second Value", widget=forms.TextInput(attrs={
        "placeholder":"Second Value Input",
        "class":"form-control"
    }))