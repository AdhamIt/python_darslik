from django.urls import path
from .views import MaktabListView
urlpatterns=[
    path('maktab/', MaktabListView.as_view(template_name='maktab.html'), name='maktab')
]