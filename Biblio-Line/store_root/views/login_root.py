from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import View


class LoginRoot(View):
    return_url = None

    def get(self, request):
        LoginRoot.return_url = request.GET.get ('return_url')
        return render (request, 'login_root.html')

    def post(self, request):
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        
        return render(request, 'root.html')

def logout(request):
    request.session.clear()
    return redirect('login')
