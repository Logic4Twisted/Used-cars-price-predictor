from django.shortcuts import render
from django.http import HttpResponseRedirect

from .model import helper

from .forms import NameForm

def get_name(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			data = form.cleaned_data
			results = helper(data)
			# return HttpResponseRedirect('/usedcars/')
			return render(request, 'thanks.html', {'d': data, 'results': results, 'no_of_results': len(results)})

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()

	return render(request, 'name.html', {'form': form})