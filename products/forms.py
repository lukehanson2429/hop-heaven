from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


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


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content', 'rating')

    content = forms.CharField(max_length=250, widget=forms.Textarea(attrs={'rows':4, 'cols':15}))

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'content': 'Content',
            'rating': 'Rating',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'review-form-input border-black rounded-0'
            self.fields[field].label = False
