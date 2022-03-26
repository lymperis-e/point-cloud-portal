from django.contrib import admin
from django.urls import path, re_path, include

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name="login"),
    path('viewer/', include('django.contrib.auth.urls')),
    re_path(r'', include('viewer.urls')),
    path('', include('pwa.urls'))
]
