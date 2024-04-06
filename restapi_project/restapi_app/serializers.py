from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


# class BookModel:
#     def __init__(self, title, publication_date, author):
#         self.title = title
#         self.publication_date = publication_date
#         self.author = author

# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length = 255)
#     publication_date = serializers.DateField()
#     author = serializers.IntegerField()

# def encode():
#     model = BookModel("New Book", "2023-12-25", 2)
#     model_serialized = BookSerializer(model)
#     print(model_serialized.data, type(model_serialized.data))
#     json = JSONRenderer().render(model_serialized.data)
#     print(json)


# def decode():
#     stream = io.BytesIO(b'{"title":"NEW BOOK", "publication_date": "2023-12-25", "author": 2}')
#     data = JSONParser().parse(stream)
#     serializer = BookSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)






