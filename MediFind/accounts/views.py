from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm


from django.shortcuts import redirect
 

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'




@login_required
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

@login_required
def patient_dashboard(request):
    return render(request, 'accounts/patient_dashboard.html')

@login_required
def vendeur_dashboard(request):
    return render(request, 'accounts/vendeur_dashboard.html')

@login_required
def personnel_sante_dashboard(request):
    return render(request, 'accounts/personnel_sante_dashboard.html')




@login_required
def dashboard(request):
    if request.user.user_type == 'admin':
        return redirect('admin_dashboard')
    elif request.user.user_type == 'patient':
        return redirect('patient_dashboard')
    elif request.user.user_type == 'vendeur':
        return redirect('vendeur_dashboard')
    elif request.user.user_type == 'personnelSante':
        return redirect('personnel_sante_dashboard')
    else:
        return redirect('login')
