from django import forms
from client.models import adsDetails, clientDetails

class adsDetailsForm(forms.ModelForm):
	class Meta:
		model= adsDetails
		fields = '__all__'
		exclude = ['client_id', 'update_flag']

class clientDetailsForm(forms.ModelForm):
	class Meta:
		model= clientDetails
		fields = '__all__'
		exclude = ['client_id']