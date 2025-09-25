from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import Item, ExternalPost
from .serializers import ItemSerializer, ExternalPostSerializer
import requests
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny


# CRUD APIs for Item
class ItemListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Item.objects.all().order_by("-created_at")
    serializer_class = ItemSerializer

class ItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Example third-party integration endpoint: fetch and save posts from JSONPlaceholder
class ImportExternalPostsView(APIView):
    def get(self, request):
        url = "https://jsonplaceholder.typicode.com/posts"
        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            return Response({"error":"Failed to fetch"}, status=status.HTTP_502_BAD_GATEWAY)
        data = resp.json()
        created = 0
        for p in data:
            # create or ignore duplicates by external_id
            obj, was_created = ExternalPost.objects.get_or_create(
                external_id=p["id"],
                defaults={"title": p["title"], "body": p["body"]},
            )
            if was_created:
                created += 1
        return Response({"imported": created, "total_fetched": len(data)})

# Dashboard view for visualization
def dashboard(request):
    
    buckets = {
        "0-9": Item.objects.filter(value__gte=0, value__lte=9).count(),
        "10-49": Item.objects.filter(value__gte=10, value__lte=49).count(),
        "50-99": Item.objects.filter(value__gte=50, value__lte=99).count(),
        "100+": Item.objects.filter(value__gte=100).count(),
    }
    return render(request, "items/dashboard.html", {"buckets": buckets})


