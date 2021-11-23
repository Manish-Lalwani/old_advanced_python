from django.urls import path,include
from . import views
urlpatterns = [
    path('list/',views.get_data),
    path('update/',views.get_data)
]
