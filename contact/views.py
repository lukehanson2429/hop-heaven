from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def contact(request):
    """ Contact the Site Owner via email """
    user = request.user

    if request.method == 'POST' and request.user.is_authenticated:
        form = RatingForm(request.POST)
        # If no review currently submit rating unless form is not valid.
        if form.is_valid():
            rating = request.POST.get('rating')
            user_rating = Rating.objects.create(
                product=product, user=user, rating=rating)
            messages.success(
                request, f'Successfully added rating too {product.name}!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Please ensure form is valid!')
    else:
        form = RatingForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
