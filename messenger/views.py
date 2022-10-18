from django.shortcuts import render, redirect
from messenger.models import Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse

@login_required
def listusers(request):
    people = User.objects.all()
    context = {'people':people}
    return render(request, 'messenger/message_list.html', context)

class NewMessage(LoginRequiredMixin,CreateView):
    model = Message
    fields = ['text_message']   
    def form_valid(self,form):
        form.instance.user_origin=self.request.user
        form.instance.user_destination = User.objects.get(id=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)
    def get_success_url(self) -> str:
        messages.success(self.request, ('Mensaje enviado con éxito!'))
        return reverse_lazy('messenger:list-messages')

@login_required
def Inbox(request):
    pms = Message.objects.filter(user_destination_id=request.user).order_by('-pub_date')
    context = {'pms':pms}
    return render(request, 'messenger/inbox.html', context)