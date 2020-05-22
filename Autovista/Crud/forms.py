from  django.forms import ModelForm	
from Crud.models import Leads

class LeadForm(ModelForm):
	class Meta:
		model = Leads
		fields= '__all__'
	