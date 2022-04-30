from django.urls import path
from .views import PostView, newPageView
urlpatterns = [
    path('news/', PostView.as_view(template_name='index.html'), name= 'news'),
    path('yangilik/', newPageView, name='yangilik')
]