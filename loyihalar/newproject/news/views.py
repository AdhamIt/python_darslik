from django.shortcuts import render
from django.views.generic import View
from django.template import loader
# Create your views here.
class PostView(View):
    template=loader.get_template('index.html')