from django import forms
from .models import Artist, Book, Music


class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ('name',)


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title',)


class MusicForm(forms.ModelForm):

    class Meta:
        model = Music
        fields = ('title', 'album',)
