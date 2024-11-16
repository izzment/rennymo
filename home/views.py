from django.shortcuts import render
from django.views import View

from .models import Event
from .forms import MessageForm

# Create your views here.

class StartingPageView(View):
    def get(self, request):
        events = Event.objects.all().order_by('-date')

        context = {
            'events': events,
            'contact_form': MessageForm()
        }
        return render(request, 'page/index.html', context)

    def post(self, request):
        events = Event.objects.all().order_by('-date')
        contact_form = MessageForm(request.POST)
        context = {
            'events': events,
            'contact_form': MessageForm()
        }

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.save()
            return render(request, 'page/index.html', context)

        return render(request, 'page/index.html', context)
