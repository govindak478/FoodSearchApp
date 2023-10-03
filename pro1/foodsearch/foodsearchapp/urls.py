from django.urls import path
from foodsearchapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('foodsearchapp.urls')),
    path('',views.product_filter,name='product_filter'),  # Include your app's URLs here
    # Other URL patterns for your project
]
