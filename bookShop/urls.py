from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from app.views import Signup

urlpatterns = [

  path('admin/', admin.site.urls),
  path('app/', include('app.urls')),

  path('accounts/', include('django.contrib.auth.urls')),
  path("accounts/signup/", Signup.as_view(), name="signup"),

  # add URL maps to redirect the base URL to the App
  path('', RedirectView.as_view(url='app/', permanent=True)),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
