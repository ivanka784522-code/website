from django.urls import path



from .views import home, room 

urlpatterns = [
    path('home/', home, name='home'),
    path('room/<slug:pk>/', room , name='room')
]
