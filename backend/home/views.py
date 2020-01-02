from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    text = request.GET.get("text", "")

    return JsonResponse({"count": len(text)})
