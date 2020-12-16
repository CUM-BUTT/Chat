from django.urls import path, include
from .views import index, log_out, log_in, sign_in

urlpatterns = [
    path('', index, name='home'),
    path('log_in', log_in, name='log_in'),
    path('sign_in', sign_in, name='sign_in'),
    path('log_out', log_out, name='log_out'),
]