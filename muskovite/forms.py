from django import forms
from .models import Meep
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper


class MeepForm(forms.ModelForm):
    body = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={
           "placeholder": "Enter your Meeping Meep...!!!",
           "class":"form-control",
           }
            ),
           label="",
        )

    class Meta:
        model = Meep
        exclude = ("user",)


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_action = reverse_lazy('register')
        self.helper.add_input(Submit('submit', 'Submit'))

    email = forms.EmailField(label="Your Email Address", widget=forms.TextInput(
        attrs={
        'class':'form-control mb-2', 
        }
        ))
    first_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(
        attrs={
        'class':'form-control mb-2', 
        }
        ))
    last_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(
        attrs={
        'class':'form-control mb-2', 
        }
        ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
    
