from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
]
''' 
    path - arguments
        1. route (required) - that contains a url pattern
        2. view (required) - calls the specified view function with an HttpRequest object
        3. name 
        4. kwargs


'''