from django import forms
from .models import Plant, Comment


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = [
            'name',
            'about',
            'used_for',
            'image',
            'category',
            'is_edible',
            'countries'
        ]
        widgets = {
            "countries": forms.CheckboxSelectMultiple(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model  = Comment
        fields = [
            "name", 
            "content"
            ]
        
        widgets = {
            "name":    forms.TextInput(attrs={"placeholder": "Your name", "minlength": "3"}),
            "content": forms.Textarea(attrs={"placeholder": "Add your comment here…", "minlength": "3", "rows": 4}),
        }