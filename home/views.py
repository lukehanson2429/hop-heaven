from django.shortcuts import render

# Create your views here.

def index(request):
    """ render view index.html """

    return render(request, 'home/index.html')
