# api/urls.py

from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from api import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/$', views.UserView.as_view()),
    url(r'^faces/$', views.FacesView.as_view()),
    url(r'^faces/(?P<visitorname>.*)/$', views.VFaceView.as_view()),
    url(r'^visitors/$', views.VisitorsView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)