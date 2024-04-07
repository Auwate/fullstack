from . import views

from django.urls import path

urlpatterns = [
    path('', view=views.getRoutes, name="routes"), # Index
    path('get/', view=views.getResponse, name='get'), # Gets the result
    path('recent/', view=views.getRecentQueries, name='recent') # Gets queries
]