from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from .models import Communication
from .forms import CommunicationForm
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

@method_decorator(login_required, name='dispatch')
class CreateCommunicationView(CreateView):
    model = Communication
    form_class = CommunicationForm
    template_name = 'assign/communication_create.html'
    success_url = reverse_lazy('create_communication')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='Nurses').exists():
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.nurse = self.request.user
        return super().form_valid(form)




@method_decorator(login_required, name='dispatch')
class CommunicationListView(ListView):
    model = Communication
    template_name = 'assign/communications.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Nurses').exists():
            return Communication.objects.filter(nurse=self.request.user)
        elif self.request.user.groups.filter(name='Patients').exists():
            return Communication.objects.filter(patient=self.request.user)
        else:
            return Communication.objects.none()

@method_decorator(login_required, name='dispatch')
class CommunicationDetailView(DetailView):
    model = Communication
    template_name = 'assign/communications_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.filter(name='Nurses').exists():
            context['patient'] = self.object.patient
        elif self.request.user.groups.filter(name='Patients').exists():
            context['nurse'] = self.object.nurse
        return context


