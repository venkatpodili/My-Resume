import request
from django.shortcuts import render, render_to_response, redirect

def myresume(request):
    return_data = {}
    return render (request, 'index.html', return_data)