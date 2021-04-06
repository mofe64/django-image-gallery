from django.shortcuts import render

# Create your views here.
from .models import Image


def index(request):
    images = Image.objects.order_by('publish_date')
    context = {
        'images': images
    }
    return render(request, 'index.html', context)
