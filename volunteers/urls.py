from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('base/', views.baseView, name='base'),  # Ensure 'base/' is mapped
    path('', views.dashboard, name='dashboard'),
    path('events/', views.eventsView, name='events'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.volunteer_list, name='volunteers'),  # Add the view for listing volunteers
]
