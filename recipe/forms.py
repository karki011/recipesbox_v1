from django.forms import ModelForm
from .models import Recipe, Author


# class RecipeAddForm(forms.Form):
#     title = forms.CharField(max_length=50, required=True)
#     description = forms.CharField(widget=forms.Textarea, required=True)
#     time_required = forms.CharField(max_length=50, required=True)
#     instructions = forms.CharField(widget=forms.Textarea, required=True)
#     imageUrl = forms.CharField(max_length=256, required=False)
#     author = forms.ModelChoiceField(queryset=Author.objects.all())

class RecipeAddForm(ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'


class AuthorAddForm(ModelForm):

    class Meta:
        model = Author
        fields = '__all__'
