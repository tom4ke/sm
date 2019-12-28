from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import city_choices, category_choices
from listings.models import Listing
from moderators.models import Moderator

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    # print(categories)
    context = {
        'category_choices' : category_choices,
        'listings' : listings,
        'city_choices' : city_choices,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all moderator
    moderators = Moderator.objects.order_by('-hire_date')
    administrators = Moderator.objects.order_by('-email')[:1]
    
    context = {
        'moderators': moderators,
        'administrators': administrators
    }
    return render(request, 'pages/about.html', context)