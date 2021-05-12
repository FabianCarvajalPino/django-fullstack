from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('shows/new', views.new_show),
    path('shows', views.displayShows),
    path('shows/create', views.create),
    path('shows/<int:idShow>', views.show),
    path('shows/<int:idShow>/edit', views.edit),
    path('shows/<int:idShow>/update', views.update),
    path('shows/<int:idShow>/destroy', views.destroy)
]