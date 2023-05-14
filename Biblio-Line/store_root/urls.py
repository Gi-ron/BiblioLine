from django.contrib import admin
from django.urls import path
from .views.root import AddAdministrator
from .views.login_root import LoginRoot

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AddAdministrator.as_view(), name=''),
    path('root', LoginRoot.as_view(), name='root'),

]
