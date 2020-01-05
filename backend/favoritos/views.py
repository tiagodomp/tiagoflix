from django.shortcuts import render
from django.http import JsonResponse


def favoritos(request):
    text = request.GET.get("text", "")

    return JsonResponse({"favoritos": len(text)})
