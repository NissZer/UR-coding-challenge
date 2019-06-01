from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home')
]
