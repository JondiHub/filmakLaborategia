from django.shortcuts import render_to_response, get_object_or_404

from django.template import RequestContext
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from filmak.models import Filma

# Create your views here.

def hasierakoOrria(request):
	return render_to_response('filmak/hasierakoOrria.html')

def hasierakoMenuaLogged(request):
	return render_to_response('filmak/hasierakoMenuaLogged.html')

def index(request):
	film_guztiak = Filma.objects.all()
	#	t = loader.get_template('filmak/index.html')
	#	c = Context({'film_guztiak': film_guztiak,})
	return render_to_response('filmak/index.html', {'film_guztiak': film_guztiak})

def detail(request, filma_id):
	f = get_object_or_404(Filma, pk=filma_id)
	return render_to_response('filmak/detail.html', {'film': f})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'filmak/signup.html', {'form': form})

def loginForm(request):
	return render_to_response('filmak/login.html', {}, context_instance=RequestContext(request))

def loginEgin(request):
	erabiltzailea = request.POST['erabiltzaileaInput']
	pasahitza = request.POST['pasahitzaInput']
	user = authenticate(username=erabiltzailea, password=pasahitza)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('/filmak/')
		else:
			return render_to_response('filmak/hasierakoOrria.html',{'error_message': "Kontua desgaituta dago."}, context_instance=RequestContext(request))
	else:
		return render_to_response('filmak/hasierakoOrria.html',{'error_message': "Login desegokia."}, context_instance=RequestContext(request))
