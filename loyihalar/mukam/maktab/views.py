from django.views.generic import ListView
from .models import Maktab
# Create your views here.
class MaktabListView(ListView):
    model=Maktab
    queryset=Maktab.objects.all()