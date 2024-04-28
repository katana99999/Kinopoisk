from django.contrib import admin
from kinopoisk.models import *

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'rating',

    )