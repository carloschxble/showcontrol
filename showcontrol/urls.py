from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/login/', permanent=False)),  # Redirige raíz a /login/
    path('', include('apps.core.urls')),
    path('', include('apps.users.urls')),
]
