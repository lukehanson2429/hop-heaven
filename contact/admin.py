from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    """ Display model data in Admin """
    list_display = (
        'user',
        'email',
        'subject',
        'message',
        'date_sent'
    )


admin.site.register(Contact, ContactAdmin)
