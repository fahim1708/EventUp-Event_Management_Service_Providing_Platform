from django import forms
from .models import Order_Info

class OrderInfoForm(forms.ModelForm):
    class Meta:
        model = Order_Info
        fields = ['full_name', 'email', 'total_Price', 'phone_no', 'date_from', 'date_to', 'address', 'district', 'thana']
        widgets = {
            'full_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'readonly': 'readonly'}),
        }
