
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import (
RegisterSerializer,ItemSerializer,
ItemDetailsSerializer,
)
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsStaffOrUser
from items.models import Item
# Create your views here.
class Register(CreateAPIView):
    serializer_class = RegisterSerializer
class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny,]
    filter_backends = [SearchFilter, OrderingFilter,]
    search_fields = ['name']
class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsStaffOrUser,]
