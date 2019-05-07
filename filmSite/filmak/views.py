from django.shortcuts import render_to_response, get_object_or_404

from filmak.models import Filma

# Create your views here.

def index(request):
	film_guztiak = Filma.objects.all()
	#	t = loader.get_template('filmak/index.html')
	#	c = Context({'film_guztiak': film_guztiak,})
	return render_to_response('filmak/index.html', {'film_guztiak': film_guztiak})

def detail(request, filma_id):
	f = get_object_or_404(Filma, pk=filma_id)
	return render_to_response('filmak/detail.html', {'film': f})
