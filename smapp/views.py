from django.shortcuts import render, redirect
from smapp.models import *
from itertools import groupby



def delete_same(list):
  return [el for el, _ in groupby(list)]

def index(request, category='Бар'):
  category = 'Бар'
  mode_counter = 0

  items = Items.objects.all()

  if 'quantity' in request.POST:
    mode_counter += 1
  
  item = items.filter(category=category)[mode_counter]

  context = {
    'item': item,
    'unit': item.unit,
    'next_mode_counter': mode_counter + 1,
    'previous_mode_counter': mode_counter - 1,
    'category': category,
  }

  return render(request, 'index.html', context)

def list(request):
  items = Items.objects.all()
  categories = delete_same([item.category for item in items])
  items_by_categories = [{'items': items.filter(category=category), 'category': category} for category in categories]

  mode_counter = 0

  context = {
    'items_by_categories': items_by_categories
  }

  if request.POST:
    quantities = request.POST
    print(quantities)
    category = request.POST['category']
    category_items = items.filter(category=category)
    for item in category_items:
      item.quantity = float(quantities[item.name])
      print(item.rule - item.quantity)
      item.save()
    
    
    


  return render(request, 'list.html', context)