from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

# 1️⃣ GET /api/items/ → Return all items
@api_view(['GET'])
def get_items(request):
    search_query = request.GET.get('search', '')
    items = Item.objects.filter(name__icontains=search_query) if search_query else Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

# 2️⃣ POST /api/items/add/ → Add a new item
@api_view(['POST'])
def add_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 3️⃣ GET /api/items/<int:item_id>/ → Get a single item
@api_view(['GET'])
def get_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    serializer = ItemSerializer(item)
    return Response(serializer.data)

# 4️⃣ PUT /api/items/update/<int:item_id>/ → Update an item
@api_view(['PUT'])
def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 5️⃣ DELETE /api/items/delete/<int:item_id>/ → Delete an item
@api_view(['DELETE'])
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
