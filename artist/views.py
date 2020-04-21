from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from django.forms import inlineformset_factory
from .models import Artist, Book, Music
from .forms import ArtistForm, BookForm, MusicForm


def artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    books = Book.objects.filter(artist=artist)
    musics = Music.objects.filter(artist=artist)
    return render(request, 'artist/artist.html', {'artist': artist, 'books': books, 'musics': musics})


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artist/artist_list.html', {'artists': artists})


def artist_new(request):
    BookFormSet = inlineformset_factory(Artist, Book, form=BookForm, extra=3, can_delete=False)
    MusicFormSet = inlineformset_factory(Artist, Music, form=MusicForm, extra=3, can_delete=False)
    if request.method == 'POST':
        artist_form = ArtistForm(request.POST, prefix='artist')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='book')
        music_formset = MusicFormSet(request.POST, request.FILES, prefix='music')
        if all([artist_form.is_valid(), book_formset.is_valid(), music_formset.is_valid()]):
            artist = artist_form.save(commit=False)
            artist.added_by = request.user
            artist.date_added = timezone.now()
            artist.save()
            # Recreate book_formset bound to the new artist instance
            book_formset = BookFormSet(request.POST, request.FILES, prefix='book', instance=artist)
            book_formset.save()
            # Recreate music_formset bound to the new artist instance
            music_formset = MusicFormSet(request.POST, request.FILES, prefix='music', instance=artist)
            music_formset.save()
            return redirect('artist', pk=artist.pk)
        else:
            return render(request, 'artist/artist_edit.html', {
                'artist_form': artist_form,
                'book_formset': book_formset,
                'music_formset': music_formset,
            })
    else:
        artist_form = ArtistForm(prefix='artist')
        book_formset = BookFormSet(prefix='book')
        music_formset = MusicFormSet(prefix='music')
        return render(request, 'artist/artist_edit.html', {
            'artist_form': artist_form,
            'book_formset': book_formset,
            'music_formset': music_formset,
        })


def artist_edit(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    BookFormSet = inlineformset_factory(Artist, Book, form=BookForm, extra=1)
    MusicFormSet = inlineformset_factory(Artist, Music, form=MusicForm, extra=1)
    if request.method == 'POST':
        artist_form = ArtistForm(request.POST, instance=artist, prefix='artist')
        book_formset = BookFormSet(request.POST, request.FILES, instance=artist, prefix='book')
        music_formset = MusicFormSet(request.POST, request.FILES, instance=artist, prefix='music')
        if all([artist_form.is_valid(), book_formset.is_valid(), music_formset.is_valid()]):
            artist = artist_form.save(commit=False)
            artist.date_edited = timezone.now()
            artist.save()
            book_formset.save()
            music_formset.save()

            return redirect('artist', pk=artist.pk)
    else:
        artist_form = ArtistForm(instance=artist, prefix='artist')
        book_formset = BookFormSet(instance=artist, prefix='book')
        music_formset = MusicFormSet(instance=artist, prefix='music')

    return render(request, 'artist/artist_edit.html', {
        'artist_form': artist_form,
        'book_formset': book_formset,
        'music_formset': music_formset,
    })
