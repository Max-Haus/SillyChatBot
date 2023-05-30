from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = 'index'),
    path('get_bot_response',views.get_bot_response ,name='get_bot_response ')
    
]