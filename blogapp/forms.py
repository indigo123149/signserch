from django import forms

from .models import MyDate

class MyDateForm(forms.ModelForm):

    class Meta:
        model = MyDate
        fields = ('year','month','day')
