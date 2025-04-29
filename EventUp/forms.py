from django import forms
from Decoration.models import Profile

class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ['phone', 'order_phone', 'district', 'thana', 'address', 'profile_picture']
