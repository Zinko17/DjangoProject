from django.urls import path
from .views import *

urlpatterns = [
    path('card_create/', cardCreate,name='card_crete'),
    path('increment/', incrementBalance,name='incr'),
    path('transaction/', transactionPage,name='transaction'),

]