from django import forms
from .models import Task

class PostForm(forms.ModelForm):
	completed = forms.BooleanField(required=False)



	class Meta:
		model = Task
		fields = ('task_name','task_details','completed')