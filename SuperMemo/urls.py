from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

"""
Пути в глобальном плане, ведет в другие приложения
"""

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),

    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('userpage/', include('userpage.urls')),
    path('courses/', include('courses.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
