from django.contrib import admin
from django.urls import path
from .views.root import AddAdministrator
from .views.login_root import LoginRoot
from .views.change_root_password import ChangeRootPassword

urlpatterns = [
    path('admin/', admin.site.urls),
    path('root1', AddAdministrator.as_view(), name='root1'),
    path('root', LoginRoot.as_view(), name='root'),
    path('root_password', ChangeRootPassword.as_view(), name = 'root_password' )

]
