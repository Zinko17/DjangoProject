from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', profile_page,name='profile'),
    path('order/<int:service_id>',order_page,name='order'),
    path('order/',my_orders,name='my_orders'),
    path('delete_order/<int:order_id>/',delete_order,name='delete_order'),
    path('update_order/<int:order_id>/',update_order,name='update_order'),
    path('update_profile/',update_profile,name='update_profile')
]
