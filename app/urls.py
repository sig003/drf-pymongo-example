from django.urls import path

from .views import Mongo

urlpatterns = [
	path('mongo/',Mongo.as_view()),
]