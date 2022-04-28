from django.forms import ModelForm
from .models import Recall

class RecallForm(ModelForm):
  class Meta:
    model = Recall
    fields = ['date', 'degree']