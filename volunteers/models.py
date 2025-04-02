from django.contrib.auth.models import User
from django.db import models

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django User model
    full_name = models.CharField(max_length=100, default="Unknown")
    phone = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='volunteer_pics/', default='default.jpg')
    joined_date = models.DateField(auto_now_add=True)  # Automatically set when created

    def __str__(self):
        return self.full_name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Task(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.volunteer.full_name} - {self.event.title}"
