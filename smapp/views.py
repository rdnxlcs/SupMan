from django.shortcuts import render
from smapp.models import *

def index(request):
    

  return render(request, 'index.html')

def list(request):
  items = Items.objects.all()
  categories = [item.category for item in items]
  items_by_categories = [{'items': items.filter(category=category), 'category': category} for category in categories]

  context = {
    'items_by_categories': items_by_categories
  }

  if 'mode' in request.POST:
    return render(request, 'index.html', {'items': item})

  return render(request, 'list.html', context)