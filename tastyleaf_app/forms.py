from django import forms
from models import *

class StoryForm(forms.ModelForm):
    author = forms.CharField(max_length=100, required=False)
    fullstory = forms.CharField(max_length=1000)
    home = forms.CharField(max_length=100, required=False)
    imgurl = forms.CharField(max_length=300)
    class Meta:
        model = Story
        fields = ('author', 'fullstory', 'question', 'home', 'imgurl')
        exclude = ['quote', 'approved']
