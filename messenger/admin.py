from django.contrib import admin
from messenger.models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('user_origin', 'user_destination','pub_date','text_message')

admin.site.register(Message, MessageAdmin)