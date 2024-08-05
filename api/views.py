from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from api.models import Item

def item_list(request):
    items = Item.objects.all()
    data = {
        "items": list(items.values("id", "name", "description"))
    }
    return JsonResponse(data)

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    data = {"id": item.id, "name": item.name, "description": item.description}
    return JsonResponse(data)