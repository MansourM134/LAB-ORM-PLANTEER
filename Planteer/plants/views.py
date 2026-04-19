from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .forms import PlantForm
from .models import Plant


def plants_view(request: HttpRequest):
    plants = Plant.objects.all().order_by('-created_at')

    category = request.GET.get('category', '')
    edible = request.GET.get('edible', '')

    if category:
        plants = plants.filter(category=category)
    if edible == 'true':
        plants = plants.filter(is_edible=True)
    elif edible == 'false':
        plants = plants.filter(is_edible=False)

    return render(request, 'plants/all_plants.html', {'plants': plants,'categories': Plant.CategoryChoices.choices,'selected_category': category,'selected_edible': edible,})


def add_plants_view(request: HttpRequest):
    plant_form = PlantForm()

    if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('plants:plants_view')
        else:
            print("form not valid:", plant_form.errors)

    return render(request, "plants/add_plants.html", {"form": plant_form})


def plant_detail_view(request: HttpRequest, plant_id: int):
    plant = get_object_or_404(Plant, id=plant_id)
    related = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:3]
    return render(request, "plants/plant_detail.html", {"plant": plant, "related": related})


def plant_update_view(request: HttpRequest, plant_id: int):
    plant = get_object_or_404(Plant, id=plant_id)
    plant_form = PlantForm(instance=plant)

    if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES, instance=plant)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('plants:plant_detail_view', plant_id=plant.id)
        else:
            print("form not valid:", plant_form.errors)

    return render(request, "plants/plant_update.html", {"form": plant_form, "plant": plant})


def plant_delete_view(request: HttpRequest, plant_id: int):
    plant = get_object_or_404(Plant, id=plant_id)

    if request.method == "POST":
        plant.delete()
        return redirect('plants:plants_view')

    return render(request, "plants/plant_delete.html", {"plant": plant})


def plant_search_view(request: HttpRequest):
    query = request.GET.get("q", "").strip()

    if query:
        results = Plant.objects.filter(name__icontains=query)
    else:
        results = []

    return render(request, "plants/plant_search.html", {
        "results": results,
        "query": query,
    })
