from django import forms
from .models import *

class show_form(forms.Form):
    sit_ups = forms.IntegerField(max_value=4)
    push_ups = forms.IntegerField(max_value=4)



