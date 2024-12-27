from django.shortcuts import render
from .models import Item
# Create your views here.

def display_item(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items' : items})
