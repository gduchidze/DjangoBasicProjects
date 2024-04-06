
# from .serializers import BookSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.forms import model_to_dict
from .models import Book
from rest_framework import generics
from .serializers import BookSerializer
# from .models import Book

# class BookAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookAPIView(APIView):
    def get(self, request):
        lst = Book.objects.all()
        return Response({'books': BookSerializer(lst, many=True).data})

    def post(self, request):
        new_book = Book.objects.create(
            title = request.data['title'],
            publication_date = request.data['publication_date'],
            author_id = request.data['author_id']
        )


        return Response({'book': BookSerializer(new_book).data })



