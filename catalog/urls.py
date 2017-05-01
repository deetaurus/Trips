from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^status/$', views.TripsList.as_view()),
]
