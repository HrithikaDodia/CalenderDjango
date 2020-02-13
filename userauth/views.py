from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegisterForm
# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(data = request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Done')
	else:
		form = UserRegisterForm()
	return render(request, 'registration/register.html', {'form': form})	

def index(request):
	return render(request, 'index.html', {})