from django.urls import path
from . import views


urlpatterns = [
    path('', views.login),
    path('main', views.main_page),
    path('news', views.life_class),
    path('calls', views.calls),
    path('lesson', views.lesson),
    path('login', views.login),
    path('user', views.user_class_list),
    path('helper_views', views.helper_views),
    path('helper', views.helper),
    path('mathematics', views.mathematics),
    path('update', views.update),
    path('russian', views.russian),
    path('physics', views.physics),
]