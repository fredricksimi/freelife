from django.urls import path
from . import views

app_name = 'day'
urlpatterns = [
	path('day', views.home_view, name='home'),
]