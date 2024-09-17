from django.urls import path
from .views import SignUpView, CustomLoginView,dashboard,admin_dashboard,patient_dashboard,vendeur_dashboard,personnel_sante_dashboard

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('admin/', admin_dashboard, name='admin_dashboard'),
    path('patient/', patient_dashboard, name='patient_dashboard'),
    path('vendeur/', vendeur_dashboard, name='vendeur_dashboard'),
    path('personnel-sante/', personnel_sante_dashboard, name='personnel_sante_dashboard'),
]
