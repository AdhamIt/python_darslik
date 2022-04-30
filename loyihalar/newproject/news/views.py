from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post
# Create your views here.
class PostView(ListView):
    # template=loader.get_template('index.html')
    # queryset=post
    model=Post
    # telplate_name='index.html'
    # context_object_name='all_post_list'

def newPageView(request):
    return HttpResponse('Hello world')
