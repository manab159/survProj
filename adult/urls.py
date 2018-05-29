from django.urls import path

from . import views


app_name='adult'
urlpatterns = [
    path('', views.index, name='index'),
    path('popStats', views.popStats, name='popStats'),
    # path('addMovie', views.addMovie, name='addMovie'),
    # path('editMovie', views.editMovie, name='editMovie'),
    # path('moviesEdit', views.moviesEdit, name='moviesEdit'),
]