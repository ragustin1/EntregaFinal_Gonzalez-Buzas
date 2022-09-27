
from django.urls import path
from .views import ThreadList, ThreadDetail, add_message, start_thread

urlpatterns = [
    path('', ThreadList.as_view(), name='list'),
    path('thread/<int:pk>/', ThreadDetail.as_view(), name='detail'),
    path('thread/<int:pk>/add', add_message, name='add_message'),
    path('thread/start/<username>/', start_thread, name="start_conversation"),
]