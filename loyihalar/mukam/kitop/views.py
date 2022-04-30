from django.shortcuts import render
from django.views.generic import ListView
from .models import Kitop
# Create your views here.
class KitopListView(ListView):
    model=Kitop
    queryset=Kitop.objects.all()