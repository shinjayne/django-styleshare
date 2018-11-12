# rest framework
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

# models
from goods.models import Goods

# serializers
from goods.serializers import GoodsListSerializer, GoodsSerializer

# Create your views here.


class GoodsListAPI(generics.ListAPIView):
	"""
	Goods List API Endpoint
	"""
	queryset = Goods.objects.all().prefetch_related('provider')
	serializer_class = GoodsListSerializer
	permission_classes = [AllowAny]


class GoodsRetrieveAPI(generics.RetrieveAPIView):
	"""
	Goods Retrieve API Endpoint
	"""
	queryset = Goods.objects.all()
	serializer_class = GoodsSerializer
	permission_classes = [AllowAny]