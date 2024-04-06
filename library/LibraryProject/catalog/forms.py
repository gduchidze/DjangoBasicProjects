from django import forms
from .models import Book

# class addBookForm(forms.Form):
#     title = forms.CharField(label="Title: ", max_length=100)
#     Author = forms.CharField(label="Author: ", max_length=100)
#     published_year = forms.IntegerField(label="Published Year: ")
#     Genre = forms.CharField(label="Genre: ", max_length=20)

class addBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year', 'genre']