from django import forms
from .models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('rating',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'rating': 'Rating',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'rating-form-input border-black rounded-0'
            self.fields[field].label = False