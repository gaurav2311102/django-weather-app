from django import forms

class Cityform(forms.Form):
    city = forms.CharField(label="city", max_length=20, required=True,widget = forms.TextInput(attrs={"placeholder" : "Enter city name "}))