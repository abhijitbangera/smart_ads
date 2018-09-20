from django import forms
from client.models import adsDetails

class adsDetailsForm(forms.ModelForm):
	class Meta:
		model= adsDetails
		fields = '__all__'