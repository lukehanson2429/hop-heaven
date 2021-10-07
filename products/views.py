from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Rating
from .forms import ProductForm, RatingForm

# Create your views here.

def all_products(request):
    """ A View to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A View to show product detail page   """
    product = get_object_or_404(Product, pk=product_id)

    template = 'products/product_detail.html'
    context = {
        'product': product,
    }

    return render(request, template, context)


@login_required
def add_product_rating(request, product_id):
    """ Give each product a rating when signed in """
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    # filter product ratings by user
    user_rating = Rating.objects.filter(product=product, user=user)

    if request.method == 'POST' and request.user.is_authenticated:
        form = RatingForm(request.POST)
        # If no review currently submit rating unless form is not valid.
        if form.is_valid():
            rating = request.POST.get('rating')
            user_rating = Rating.objects.create(product=product, user=user, rating=rating)
            messages.success(request, f'Successfully added rating too {product.name}!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Please ensure form is valid!')
    else:
        # If there is a rating currently for this product from current user raise an error
        if user_rating:
            # error raised
            messages.error(request, 'You have already rated this beer!')
            prev_url = request.META.get('HTTP_REFERER')
            return redirect(prev_url)
        form = RatingForm()

    template = 'products/add_product_rating.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_product_rating(request, rating_id):
    """ Edit Product Rating """
    rating = get_object_or_404(Rating, pk=rating_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form = RatingForm(request.POST, instance=rating)
            form.save()
            messages.success(request, 'Successfully Updated your rating!')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Please ensure form is valid!')
    else:
        if rating.user != request.user:
            messages.error(request, 'You cannot edit this rating!')
            prev_url = request.META.get('HTTP_REFERER')
            return redirect(prev_url)
        form = RatingForm(instance=rating)
        messages.info(request, f'You are updating your rating for {rating.product}!')

    template = 'products/edit_product_rating.html'
    context = {
        'form': form,
        'rating': rating,
    }

    return render(request, template, context)


@login_required
def delete_product_rating(request, rating_id):
    """ Delete your rating """

    rating = get_object_or_404(Rating, pk=rating_id)

    if rating.user != request.user:
        messages.error(request, 'You did not create this rating.')
        prev_url = request.META.get('HTTP_REFERER')
        return redirect(prev_url)
    else:
        rating.delete()
        messages.success(request, 'Rating deleted!')
        prev_url = request.META.get('HTTP_REFERER')
        return redirect(prev_url)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.info(request, f'Successfully added {product.name}!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add beer. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, f'Successfully updated {product.name}!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, f'Failed to update {product.name}. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.info(request, f'{product.name} Deleted!')
    return redirect(reverse('products'))
