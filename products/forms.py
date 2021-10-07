from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Rating


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 product-form-input'


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
