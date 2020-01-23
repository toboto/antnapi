from django.urls import path

from . import views

app_name = 'maps'
urlpatterns = [
    path('', views.index, name='index'),
    path('demo/', views.demo, name='demo'),
    path('<int:c>/', views.area, name='area'),
    path('hot_areas/', views.hot_areas, name='hot_areas'),
]
