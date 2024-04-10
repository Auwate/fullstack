from . import views

from django.urls import path

urlpatterns = [
    path('', view=views.getRoutes, name="routes"), # Index
    path('recent/', view=views.getRecentQueries, name='recent'), # Gets queries
    path('post/', view=views.postData, name='post') # Receives post data
]