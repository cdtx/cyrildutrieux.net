from django.shortcuts import render, render_to_response

# Create your views here.
def homePage(request):
    return render_to_response('cyrildutrieux/index.html')
