from django.urls import path
from . import views

app_name = "plants"

urlpatterns = [
    path("all/plants/",views.plants_view,name="plants_view"),
    path("add/plants/",views.add_plants_view,name="add_plants_view"),
    path("plants/<int:plant_id>/detail/",views.plant_detail_view,name="plant_detail_view"),
    path("plants/<int:plant_id>/update/",views.plant_update_view,name="plant_update_view"),
    path("plants/<int:plant_id>/delete/",views.plant_delete_view,name="plant_delete_view"),
    path("plants/search/",views.plant_search_view,name="plant_search_view"),
]