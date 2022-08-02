from django import forms 
from django.forms import ModelForm
from .models import * 


# creating a form 
class TaskTypeForm(forms.ModelForm): 

	# create meta class 
	class Meta: 
		# specify model to be used 
		model = TaskType 

		# specify fields to be used 
		fields = [ 
			"name", 
            "notes",
            "status"
		] 

class usersForm(forms.ModelForm): 

	# create meta class 
	class Meta: 
		# specify model to be used 
		model = Users 

		# specify fields to be used 
		fields = [ 
			"firstname", 
			"lastname", 
			"email", 
			"phone_number", 
			"image", 
            "about"
		] 

