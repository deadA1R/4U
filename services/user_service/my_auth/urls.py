from django.urls import path
from .views import login_cust

urlpatterns = [
    path('login/', login_cust, name='login'),
]