from .models import Books
from django import forms

class BookAddForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('title', 'genre', 'author', 'isbn', )

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'genre' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control'}),
            'isbn' : forms.TextInput(attrs={'class': 'form-control'}),
        }