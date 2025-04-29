from django.urls import path
from . import views

urlpatterns = [
    path('', views.Decoration, name='decoration'),
    path('search/', views.search_view, name='search_view'),
    path('location-autocomplete/', views.Decoration, name='location_autocomplete'),
    path('decoration/view_page/',views.view_page_decoration, name='view_page_decoration'),
    path('decoration/<int:pk>/', views.DecorationDetailView, name='decoration_detail'),
    path('confirmation/', views.ConfirmationView, name='confirmation'),
]
