from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

# Main url routing pattern, includes url routing patterns from eleni_app

urlpatterns = patterns('',
    url(r'^', include('eleni_app.urls', namespace="eleni_app")),
    url(r'^admin/', include(admin.site.urls)),
    # Routing pattern do deal with media files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)