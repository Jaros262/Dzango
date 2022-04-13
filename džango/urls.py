from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from formule import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formule/', include('formule.urls')),
    path('', RedirectView.as_view(url='formule/')),
]
