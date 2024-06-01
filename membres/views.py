from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.models import User


# Create your views here.

def connexion(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.success(request,"GDStocks : Erreur lors de la connexion!")
            return redirect('Dashboard')
    else: 
        return render(request, 'authenticate/connexion.html', {})
    
def deconnexion(request,):
    logout(request)
    messages.success(request,"Vous êtes déconnecter!")
    return redirect('connexion')

def ajouterUtilisateur(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"Utilisateur ajouté avec succées")
            return redirect('Home')
    else:
        form = RegisterUserForm()
        return render(request, 'authenticate/ajouterUtilisateur.html', {
            'form':form,
        })
    
def login_view(request):
    # Logique pour la page de connexion
    return render(request, 'connexion.html')

def listeUtilisateur(request):
    utilisateur = User.objects.all()
    return render(request, 'listeUtilisateur.html',{'utilisateur':utilisateur})


def afficherUtilisateur(request, id):
    utilisateur = get_object_or_404(User, id=id)
    return render(request, 'afficherUtilisateur.html', {'utilisateur': utilisateur})







