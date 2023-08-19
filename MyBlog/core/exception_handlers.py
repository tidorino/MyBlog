import logging

from django.http import response, HttpResponse
from django.shortcuts import render


def page_not_found_view(request, exception, *args, **kwargs):

    return render(request, '404.html', status=404)


def server_error_view_500(request, *args, **kwargs):

    return render(request, '500.html', status=500)
