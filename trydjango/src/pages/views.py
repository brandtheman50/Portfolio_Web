from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is the home"
    }
    return render(request, "home.html", my_context)
