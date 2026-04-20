from django.contrib import admin
from .models import Plant, Comment

# Register your models here.

class PlantAdmin(admin.ModelAdmin):

    list_display = ("name", "category")
    list_filter = ("category",)

class CommentAdmin(admin.ModelAdmin):

    list_display = ("name", "plant_id", "added_at")
    list_filter = ("plant_id",)


admin.site.register(Plant, PlantAdmin)
admin.site.register(Comment, CommentAdmin)