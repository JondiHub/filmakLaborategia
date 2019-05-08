from django.shortcuts import render_to_response, get_object_or_404

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


from filmak.models import Filma

# Create your views here.
def homeT(request):
	return render_to_response('orokorra/homeT.html')

def hasieraMenua(request):
	return render_to_response('filmak/hasieraMenua.html')

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
