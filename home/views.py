""" Imports  """
from django.shortcuts import render


def index(request):
    """ Render view for home page """

    return render(request, 'home/index.html')
