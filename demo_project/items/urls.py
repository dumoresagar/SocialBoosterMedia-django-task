from django.urls import path
from .views import ItemListCreateAPIView, ItemRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("", ItemListCreateAPIView.as_view(), name="item-list-create"),
    path("<int:pk>/", ItemRetrieveUpdateDestroyAPIView.as_view(), name="item-detail"),

]
