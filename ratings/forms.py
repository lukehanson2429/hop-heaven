""" Imports """
from django import forms
from .models import Rating


class RatingForm(forms.ModelForm):
    """ Rating Form  """
    class Meta:
        """ Rating field only displayed """
        model = Rating
        fields = ('rating',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'rating': 'Leave your rating between 1 - 5',
        }

        self.fields['rating'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'rating-form border-black rounded-0'
            self.fields[field].label = False
