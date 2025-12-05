from django.shortcuts import render
from review_app.models import *

def index(request):
    reviews = Review.objects.all()
    context = {
        "reviews" : reviews
    }
    return render(request,
                   template_name="reviews/index.html",
                   context=context)

# Create your views here.
