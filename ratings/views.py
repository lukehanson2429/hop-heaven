""" Imports  """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Rating
from .forms import RatingForm


@login_required
def add_rating(request, product_id):
    """ Give each product a rating when signed in """
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    # filter product ratings by user
    user_rating = Rating.objects.filter(product=product, user=user)

    # If there is a rating from current user raise an error
    if user_rating:
        # error raised
        messages.error(request, 'You have already rated this beer!')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
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

    template = 'ratings/add_rating.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_rating(request, rating_id):
    """ Edit Product Rating """
    rating = get_object_or_404(Rating, pk=rating_id)
    # User can only edit rating if created by the user
    if rating.user != request.user:
        messages.error(request, 'You are not authorized to edit this rating!')
        return redirect(reverse('home'))
    else:
        # Editing rating
        if request.method == 'POST':
            form = RatingForm(request.POST)
            # If form is valid edit rating
            if form.is_valid():
                form = RatingForm(request.POST, instance=rating)
                form.save()
                messages.success(request, 'Successfully Updated your rating!')
                return redirect(reverse('profile'))
            else:
                # If form is invalid error message is raised.
                messages.error(request, 'Please ensure form is valid!')
        # Form prefilled with exisiting rating and info message displayed.
        form = RatingForm(instance=rating)
        messages.info(request, f'You are updating \
            your rating for {rating.product}!')

    template = 'ratings/edit_rating.html'
    context = {
        'form': form,
        'rating': rating,
    }

    return render(request, template, context)


@login_required
def delete_rating(request, rating_id):
    """ Delete your rating """

    rating = get_object_or_404(Rating, pk=rating_id)
    # User can only delete rating if created by the user
    if rating.user != request.user:
        messages.error(request, 'You are not authorized to delete this rating')
        return redirect(reverse('profile'))
    else:
        # Otherwise delete rating
        rating.delete()
        messages.success(request, 'Rating deleted!')
        return redirect(reverse('profile'))
