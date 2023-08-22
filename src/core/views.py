from django.shortcuts import render, redirect
from django.urls import path, include
from django.http import HttpResponseRedirect


def home_view(request):
    return render(request, 'pages/home.html', {})

def change_theme(request, **kwargs):
    if 'is_dark_theme' in request.session:
        request.session['is_dark_theme'] = not request.session.get('is_dark_theme')
    else:
        request.session['is_dark_theme'] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))