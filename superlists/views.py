from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def super_list(request):
    return JsonResponse({
        'message': 'hello python',
        'items': ['AWS', 'Azure'],
    }, json_dumps_params={'ensure_ascii': True})
