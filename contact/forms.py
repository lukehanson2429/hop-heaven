""" Imports """
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Rating Form  """
    class Meta:
        """ Rating field only displayed """
        model = Contact
        exclude = ('user', 'date_sent',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'subject': 'Subject Title',
            'message': 'Message Body',
        }

        self.fields['message'].widget.attrs.update(style='max-height: 120px')
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'contact-form border-black rounded-0'
            self.fields[field].label = False
