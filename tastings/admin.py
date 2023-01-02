from django.contrib import admin

from .models import Event, TastingNote, Wine

class WineAdmin(admin.ModelAdmin):
    fields = ['brand',
              'producer',
              'country',
              'region',
              'name',
              'grape',
              'vintage',
              'fortified',
              'sparkling',
              'desert',
              'color']
class EventAdmin(admin.ModelAdmin):
    fields = ['title',
              'date',
              'location',
              'wines']

class TastingNoteAdmin(admin.ModelAdmin):
    fields = ['author',
              'wine',
              'event',
              'rating',
              'thoughts']

admin.site.register(Wine, WineAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(TastingNote, TastingNoteAdmin)
