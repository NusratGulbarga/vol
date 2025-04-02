from django.contrib import admin
from .models import Volunteer, Event, Task
from .models import Event  # Import the Event model

admin.site.register(Volunteer)
admin.site.register(Task)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')  # Display these fields in admin
