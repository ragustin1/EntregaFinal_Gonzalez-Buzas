from django.urls import path, include

from messenger.views import *


app_name = 'messengers'


urlpatterns = [
    # Django's defaults auth urls login/logout
    path('', include('django.contrib.auth.urls')),

    # Registration/Modification patterns
    path('register/', register, name='register'),
    path('update/', update_profile, name='UpdateProfile'),
    path('update/avatar/', update_avatar, name='UpdateAvatar'),
    path('profile/<user_id>/', profile, name='Profile')
    
]