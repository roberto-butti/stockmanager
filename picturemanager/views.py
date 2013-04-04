# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.forms import ModelForm
from django.contrib.auth.models import User

from picturemanager.models import Picture

from pprint import pprint

class PictureForm(ModelForm):
	class Meta:
		model = Picture
		exclude = ('author')

def uploadAction(request):
	pictureForm = PictureForm()

	message = False

	if request.method == 'POST':

		# posted a form
		picture = Picture(author=User.objects.get(id=request.user.id)) # Set the picture author
		pictureForm = PictureForm(request.POST, request.FILES, instance=picture)

		if pictureForm.is_valid():
			# save the form
			pictureForm.save()

			# reset form
			pictureForm = PictureForm()

			# set success message
			message = {'class': 'success', 'text': 'Immagine caricata'}
		else:
			# form has errors
			return render(request, 'upload.html',
				{'form': pictureForm,
				'message': {'class': 'alert', 'text': 'Il form contiene errori'}})

	return render(request, 'upload.html', {'form': pictureForm, 'message': message})
