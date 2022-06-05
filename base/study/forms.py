from django.forms import ModelForm
from .models import Room

#this is RoomForms
class CreateForm(ModelForm):
    
    class Meta:
        model = Room
        fields = '__all__'
