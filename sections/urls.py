from .views import helicopter_cabin, page1
from django.urls import path, include
urlpatterns = [
    path('helicopter_cabin/',  helicopter_cabin, name="helicopter_cabin"),
    path('page1/',  page1, name="page_1"),
]














