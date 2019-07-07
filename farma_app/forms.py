from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import ItemTable
from bootstrap_datepicker_plus import DatePickerInput

class PersonForm(forms.ModelForm):
    class Meta:
        model = ItemTable
        fields = ('id', 'refno', 'slno', 'date', 'mata_name', 'manu_name', 'batch_no', 'product', 'agent', 'mfgdate', 'expdate', 'amount', 'consumption','unit', 'coa', 'msds', 'moa')
        widgets = {
            'date': DatePickerInput(), # default date-format %m/%d/%Y will be used
            'mfgdate': DatePickerInput(), # default date-format %m/%d/%Y will be used
            'expdate': DatePickerInput(), # default date-format %m/%d/%Y will be used
        }