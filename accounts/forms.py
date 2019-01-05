from django import forms
from .models import getintouch

class getintouchForm(forms.ModelForm):
    class Meta:
        model = getintouch
        fields = ('first_name',
                  'last_name',
                  'company',
                  'phone',
                  'email',
                  'website',
                  'comments',)
