from django import forms

from furry_funnies.author.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorCreateForm(AuthorBaseForm):
    class Meta:
        model = Author
        exclude = ['info', 'image_url']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'passcode': forms.PasswordInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'pets_number': forms.TextInput(attrs={'placeholder': 'Enter the number of your pets...'}),
        }

class AuthorEditForm(AuthorBaseForm):
    pass
