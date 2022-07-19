from django.contrib import admin

# Register your models here.
from .models import *

class MusicInline(admin.StackedInline):
    '''Stacked Inline View for '''
    model = Music
    min_num = 0
    max_num = 3
    extra = 1

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [ MusicInline]

