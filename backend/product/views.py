from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
import requests

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  def get_queryset(self):
    url = 'https://no2gru7ua3.execute-api.us-east-1.amazonaws.com/'
    response = requests.get(url)
    print(response)
    json = response.json()
    ls = []
    for index,produto in enumerate(json['produtos']):
      aux = {}
      aux['id'] = index
      aux['pk'] = index
      aux ['name'] = produto['produto']
      aux['description'] = produto['produto']
      aux['price'] = produto['valor']
      ls.append(aux)
    return ls