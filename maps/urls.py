from django.urls import path

from . import views

app_name = 'maps'
urlpatterns = [
    path('', views.index, name='index'),
    path('demo/', views.demo, name='demo'),
    path('baidumap/', views.baidumap, name='baidumap'),
    path('heatmap/', views.heatmap, name='heatmap'),
    path('<int:c>/', views.area, name='area'),
    path('hot_areas/', views.hot_areas, name='hot_areas'),
    path('hot_area_names/', views.hot_area_names, name='hot_area_names'),
]
