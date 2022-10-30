from django.forms import ModelForm
from .models import Appointment
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class ApointmentForm(ModelForm):
    start = forms.DateField(widget=DateInput)
    end = forms.DateField(widget=DateInput)
    class Meta:
        model = Appointment
        fields = ('__all__')

class DeleteForm(ModelForm):
    start = forms.DateField(widget=DateInput)
    class Meta:
        model = Appointment
        fields = ('room','person','start')

class FindForm(ModelForm):

    month = forms.IntegerField()
    class Meta:
        model = Appointment
        fields = ('room',)

