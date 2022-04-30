from django.urls import path
from .views import KitopListView
urlpatterns=[
    path('kitop/', KitopListView.as_view(template_name='kitop.html'), name='kitop')
]