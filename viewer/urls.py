from . import views
from django.urls import path, re_path, include




urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    path('viewer/<slug:slug>/', views.viewer, name='viewer'),
    path('3dviewer/<slug:slug>/', views.cesium_viewer, name='3dviewer'),

    path('map/', views.map_viewer, name='map_portal'),
    path('get/clouds/json/', views.user_clouds_json, name='user_clouds_json'),

    path('demo/<slug:slug>/', views.demo, name='demo')   
]