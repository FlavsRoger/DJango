from django.urls import path

from . import views

urlpatterns = [
    path('pesquisa/', include('pesquisa.urls')),
    path('admin/', admin.site.urls),
]