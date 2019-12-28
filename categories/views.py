from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from .choices import price_choices, bedroom_choices, state_choices
from .models import Category
from listings.models import Listing

def index(request):
    categories = Category.objects.order_by('-category_date')
    paginator = Paginator(categories, 30)
    page = request.GET.get('page')
    paged_categories = paginator.get_page(page)
    context = {
        'categories': paged_categories
    }
    return render(request, 'categories/categories.html', context)

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    listings = Listing.objects.filter(category=category_id)
    context = {
        'listings': listings,
        'category': category,
    }
    return render(request, 'listings/listings.html', context)