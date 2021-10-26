
from django import forms
#Implement Hashing of password
#Implement check for user already exists
class SignUpForm(forms.Form):

    gender_choice = [('M', "Male"), ('F', "Female"), ("NonBinary", "Nb")]

    uname = forms.CharField(label="username", max_length=100)
    first_name = forms.CharField(label="firstname", max_length=100)
    last_name = forms.CharField(label="firstname", max_length=100)
    gender = forms.ChoiceField(label="gender", choices=gender_choice, widget=forms.RadioSelect)
    password = forms.CharField(label="Enter password", widget=forms.PasswordInput())
    birth_date = forms.DateField(label="Enter your birth date", widget=forms.SelectDateWidget)
