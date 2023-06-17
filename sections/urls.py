from .views import get_data, aircraft, Home, page1
from django.urls import path
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('aircraft/',  aircraft, name="aircraft_info"),
    path('special_cases/',  get_data, name="special_cases"),
    path('page1/',  page1, name="page_1")  
]














