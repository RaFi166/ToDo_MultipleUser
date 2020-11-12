from django import forms
from task import models

class Taskform(forms.ModelForm):

    class Meta:
        model = models.Task
        fields = ['title', 'status', 'priority']