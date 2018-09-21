from django import forms
from client.models import adsDetails, clientDetails

class adsDetailsForm(forms.ModelForm):
	class Meta:
		model= adsDetails
		fields = '__all__'
		exclude = ['client_id']

class clientDetailsForm(forms.ModelForm):
	class Meta:
		model= clientDetails
		fields = '__all__'
		exclude = ['client_id']