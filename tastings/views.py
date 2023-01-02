from django.shortcuts import render
from .models import TastingNote, Wine, Event
import django_filters as filters
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView

User = get_user_model() 

class TastingNoteFilter(filters.FilterSet):
    wine = filters.ModelMultipleChoiceFilter(queryset=Wine.objects.all())
    author = filters.ModelMultipleChoiceFilter(queryset=User.objects.all())
    event = filters.ModelMultipleChoiceFilter(queryset=Event.objects.all())
    class Meta:
        model = TastingNote
        fields = {
            'rating': ['exact'], 
            'thoughts': ['icontains'],
        }

def tasting_notes(request):
    f = TastingNoteFilter(request.GET, queryset=TastingNote.objects.all())
    context = {
        'filter': f,
        'user': request.user,
    }
    return render(request, 'tastings/tasting_notes.html', context)

class WineList(ListView):
    model = Wine
    paginate_by = 20
    template_name = "tastings/winelist.html"

class EventList(ListView):
    model = Event
    paginate_by = 10
    template_name = "tastings/eventlist.html"
