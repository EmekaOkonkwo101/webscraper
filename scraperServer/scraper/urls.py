
from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)


urlpatterns = router.urls


manual_urlpatterns = [
    path('scrapy', views.run_scraper, name='run_scrapy'),
]

urlpatterns = manual_urlpatterns + router.urls