from django.shortcuts import render
from django.http import HttpResponseRedirect

from .model import helper

from .forms import InputForm

def get_name(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = InputForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			data = form.cleaned_data
			results = helper(data)
			return render(request, 'thanks.html', {'results': results, 'no_of_results': len(results)})

	# if a GET (or any other method) we'll create a blank form
	else:
		form = InputForm()

	return render(request, 'name.html', {'form': form})