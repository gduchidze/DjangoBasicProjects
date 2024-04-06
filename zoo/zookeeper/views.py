from django.core.cache import cache
from rest_framework import generics
from rest_framework.response import Response
from .models import Category, Animal
from .serializers import CategorySerializer, AnimalSerializer


# Create your views here.
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def list(self, request, *args, **kwargs):
        cache_key = "animals_list"
        cache_time = 60 * 5
        data = cache.get(cache_key)
        if not data:
            animals = Animal.objects.all()
            data = AnimalSerializer(animals, many=True).data
            cache.set(cache_key, data, cache_time)

        return Response(data)


class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
