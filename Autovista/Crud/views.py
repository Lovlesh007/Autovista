from django.shortcuts import render
from django.http import HttpResponse
from .forms import LeadForm


def index(request):
	form = LeadForm()
	if(request.method=='POST'):
		form = LeadForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'Crud/index.html',{'key': 'Thank You For Your Response!!'})
	else:
		return render(request,'Crud/index.html',{'form': form})
