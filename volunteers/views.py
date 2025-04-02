from django.shortcuts import render, redirect
from .models import Volunteer, Event, Task
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    volunteer = Volunteer.objects.get(user=request.user)
    tasks = Task.objects.filter(volunteer=volunteer)
    return render(request, 'dashboard.html', {'volunteer': volunteer, 'tasks': tasks})

def baseView(request):
    return render(request, 'base.html')  # Ensure 'base.html' exists in templates

def homeView(request):
    return render(request, 'home.html')  # Ensure 'home.html' exists

def eventsView(request):
    events = Event.objects.all()  # Fetch all events
    return render(request, 'events.html')  # Make sure 'events.html' exists

def volunteer_list(request):
    volunteers = Volunteer.objects.all()  # Get all volunteers
    return render(request, 'volunteers.html', {'volunteers': volunteers})

def volunteersView(request):
    volunteers = Volunteer.objects.all()  # Fetch all volunteers
    return render(request, 'volunteers.html', {'volunteers': volunteers})