# coding: utf8

from django.views.generic import ListView
from .models import Compte


class CompteListView(ListView):
    model = Compte
    template_name = 'compte_list.html'
