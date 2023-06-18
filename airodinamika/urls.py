from .views import new_page,special_cases
from django.urls import path
urlpatterns = [
    path('special_cases/', special_cases, name="special_cases"),
    path('weather/', new_page, name="weather_page")
]
