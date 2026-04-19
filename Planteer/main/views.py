from django.shortcuts import render
from django.http import HttpRequest


def home_view(request: HttpRequest):
    from plants.models import Plant
    latest_plants = Plant.objects.all().order_by('-created_at')[:3]
    return render(request, 'main/home.html', {'latest_plants': latest_plants})