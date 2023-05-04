from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import  View
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

class ChangePassword(View):
    def get(self, request):
        return render(request, "change_password.html")
    
 
    def post(self, request):
        postData = request.POST
        old_password = postData.get('old_password')
        print(old_password)
        new_password = postData.get('new_password')
        print(new_password)
        confirm_password = postData.get('old_password')
        print(confirm_password)

        return redirect('account')
    
        # # if request.method == 'POST':
        # #     form = PasswordChangeForm(request.user, request.POST)
        # #     if form.is_valid():
        # #         user = form.save()
        # #         update_session_auth_hash(request, user)
        # #         messages.success(request, 'Tu contraseña se actualizó correctamente')
        # #         return redirect('homepage')
        # #     else:
        # #         messages.error(request, 'Asegurese de corregir los errores antes de enviar la información.')
        # # else:
        # #     form = PasswordChangeForm(request.user)
        # # return render(request, 'change_password.html', {'form': form})
