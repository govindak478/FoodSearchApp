

from django.contrib import admin
from django.urls import path, include
from foodsearchapp import views


urlpatterns = [
    path('',views.product_filter, name='product_filter'),
    path('admin/', admin.site.urls),
    path('foodsearchapp/', include('foodsearchapp.urls')),
    # path('search/', views.filter_food_items, name='search_view'),  
    # path('filter_by_type/<str:type>/', views.filter_by_type, name='filter_by_type'),


]
