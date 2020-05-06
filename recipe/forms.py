from django import forms
from .models import Author, Recipe


# class RecipeAddForm(forms.Form):
#     author = forms.ModelChoiceField(queryset=Author.objects.all())
#     title = forms.CharField(max_length=50, required=True)
#     description = forms.CharField(widget=forms.Textarea, required=True)
#     time_required = forms.CharField(max_length=50, required=True)
#     instructions = forms.CharField(widget=forms.Textarea, required=True)
#     imageUrl = forms.CharField(max_length=256, required=False)


class RecipeAddForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['author', 'title', 'description',
                  'time_required', 'instructions']


class AuthorAddForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'
