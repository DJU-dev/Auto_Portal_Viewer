from django.shortcuts import render
from django.http import HttpResponse

from Achievement import achi_selenium

semester, figure = achi_selenium.achieve_data()

def scrap_here(request): 

    return render(request, 'index.html',{
        'semester': semester,
        'figure' : figure,
    })
  