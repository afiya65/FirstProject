from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# Create your views here.
def index(request):
    return render(request, 'index.html')
def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "no"
        except:
            error="yes"
    return render(request, 'admin_login.html', locals())
def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')
