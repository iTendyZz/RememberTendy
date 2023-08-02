from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ('title', 'description', 'icon', 'important')