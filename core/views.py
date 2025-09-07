from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, FormView, DetailView
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponseRedirect

from core.usac import Billed_Entity
from core.forms import BenForm

class Home(FormView):
    template_name: str = 'core/home.html'
    form_class = BenForm

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        self.form = form    
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        ben = self.form.cleaned_data['ben']
        return reverse('core:ben', kwargs={'ben': ben})

class Ben(TemplateView):
    template_name: str = 'core/ben.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ben = Billed_Entity(self.kwargs.get('id')).all
        context['ben'] = ben
        return context
