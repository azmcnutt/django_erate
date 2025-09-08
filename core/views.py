from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, FormView, DetailView
from django.db.models import Q
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from core.usac import Usac
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
        return reverse('core:ben', kwargs={'id': ben})

class Ben(TemplateView):
    template_name: str = 'core/ben.html'

    def get(self, request, *args, **kwargs):
            # Check is BEN exists.  If not, return to home and show an error
            usac = Usac()
            usac.entity.set_ben(self.kwargs.get('id'))
            self.ben = usac.entity.all
            if not self.ben:
                messages.error(request, f'Billed Entity {self.kwargs.get("id")} not Found')
                return redirect('core:home')  # Redirect to a named URL pattern
            self.ben['annexes'] = usac.annex.get_annexes(self.ben['entity_number'])
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ben'] = self.ben
        return context
