import random

from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views import generic

from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganizorAndLoginRequiredMixin


class AgentListView(OrganizorAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentCreateView(OrganizorAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizer = False
        user.set_password(f'{random.randint(0, 1000000)}')
        user.save()
        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile
        )
        send_mail(
            subject='You are invited to be an agent',
            message=f'You were invited as an agent on DJ CRM. Please login to confirm your account.',
            from_email='admin@test.com',
            recipient_list=[user.email],
        )
        return super(AgentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("agents:agent-list")


class AgentDetailView(OrganizorAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = 'agent'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentUpdateView(OrganizorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm
    context_object_name = 'agent'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_success_url(self):
        return reverse("agents:agent-list")


class AgentDeleteView(OrganizorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_success_url(self):
        return reverse("agents:agent-list")
