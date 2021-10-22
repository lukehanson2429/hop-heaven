from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm


@login_required
def contact(request):
    """ Contact the Site Owner via email """
    user = request.user

    if request.method == 'POST' and request.user.is_authenticated:
        form = ContactForm(request.POST)
        # If no review currently submit rating unless form is not valid.
        if form.is_valid():
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            contact_email = Contact.objects.create(user=user, email=email, subject=subject, message=message)
            messages.success(
                request, 'Thanks for getting in touch!')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Please ensure form is valid!')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
