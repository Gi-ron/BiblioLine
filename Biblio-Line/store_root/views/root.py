from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import View
from store_root.models.root import Root
from django.contrib.auth.hashers import make_password


class AddAdministrator(View):

    def get(self, request):
        
        return render (request, 'root.html')
    
    def post(self, request):
        email = request.POST.get ('email')
        password = request.POST.get ('dni')
        username = request.POST.get ('name')
        
        root = Root(email=email,
                    password=password,
                    username=username)
        root.password = make_password(root.password)
        
        root.register()
        return redirect('homepage')
        
         
        
        