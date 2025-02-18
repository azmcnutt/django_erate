from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class login(TemplateView):
    template_name = "project/login.html"
class about(TemplateView):
    template_name = "project/about.html"
#@login_required
#class home(TemplateView):
#    template_name = "project/home.html"
# @login_required
# def home(request):
#     link = Link.objects.all()
#     return render(request, 'project/home.html', {'link': link})

class Home(LoginRequiredMixin, TemplateView):
    template_name: str = 'project/home.html'

    def get_queryset(self, **kwargs):
        user = self.request.user
        qs = super().get_queryset(**kwargs)
        return qs.filter(enabled=True).filter(
            Q(group__in=user.groups.all())
            | Q(group__isnull=True))