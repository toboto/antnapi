from django.urls import path

from . import views

app_name = 'maps'
urlpatterns = [
    path('', views.index, name='index'),
    path('demo/', views.demo, name='demo'),
    path('<int:c>/', views.area, name='area'),
    path('areas/<int:c1>/<int:c2>/', views.areas, name='areas'),
]
