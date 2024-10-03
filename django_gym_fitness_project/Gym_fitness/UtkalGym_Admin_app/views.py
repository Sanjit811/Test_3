from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'UtkalGym_Admin_app/index.html')
