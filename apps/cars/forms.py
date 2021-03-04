from django.forms import ModelForm, DateTimeInput

from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['date_start', 'date_finish']
        widgets = {
            'date_start': DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'date_finish': DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
        }

