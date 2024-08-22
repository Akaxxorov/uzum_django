from django.urls import path
from .views import product_list , product_detali


urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:id>/', product_detali, name='product_detail')
]
