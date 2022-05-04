from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from app import views as app_views

urlpatterns = [

  path('admin/', admin.site.urls),
  path('app/', include('app.urls')),

  path('accounts/', include('django.contrib.auth.urls')),
  path("accounts/signup/", app_views.Signup.as_view(), name="signup"),
  
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
