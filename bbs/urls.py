from django.conf.urls import include, url
from django.contrib import admin
from web import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^web/', include('web.urls')),
    url(r'^', include('web.urls')),
]


