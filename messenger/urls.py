from django.urls import path
from . import views

app_name='messenger'
urlpatterns = [
    path('messages', views.Inbox, name='list-messages'),
    path('message/send/<pk>',views.NewMessage.as_view(), name="send_messages"),
    path('message/list_users',views.listusers, name="list-users"),
    ]    