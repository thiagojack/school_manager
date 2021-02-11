from django.urls import path
from . import views

app_name = 'grids'
urlpatterns = [
    path('', views.GridView.as_view(), name='grid'),
]