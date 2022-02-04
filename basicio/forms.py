
from django import forms
#Implement Hashing of password
#Implement check for user already exists
class SignUpForm(forms.Form):

    gender_choice = [('M', "Male"), ('F', "Female"), ("Nb", "Non Binary")]

    uname = forms.CharField(label="username", max_length=100)
    first_name = forms.CharField(label="firstname", max_length=100)
    last_name = forms.CharField(label="lastname", max_length=100)
    gender = forms.ChoiceField(label="gender", choices=gender_choice, widget=forms.RadioSelect)
    password = forms.CharField(label="Enter password", widget=forms.PasswordInput())
    birth_date = forms.DateField(label="Enter your birth date", widget=forms.SelectDateWidget(years=range(1900,2100)))
    emailId = forms.EmailField(label="Enter Email ID")

class LoginForm(forms.Form):
    uname = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Enter Password", widget=forms.PasswordInput())

class CreateHubForm(forms.Form):
    hubname = forms.CharField(label="hubname", max_length=50)
    hubdesc = forms.CharField(label="hubdesc", max_length=300)
