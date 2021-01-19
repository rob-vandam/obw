from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from .models import Profile
#from .models import LedenLijst,LedenProfiel

@login_required(login_url='/admin/login/')
def edit_profile_page(request):
    profiel = request.user.id
    return render(request, 'edit-profiel.html',{'profiel':profiel})
