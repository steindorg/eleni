from django.conf.urls import patterns, url
from django.conf import settings

from eleni_app.views import project, project_details, about, contact, enter, eleni, links

#Main url routing patterns

urlpatterns = patterns('',
    # Examples:
    url(r'^$', enter),
    url(r'^home/$', eleni),
    url(r'^theatre/$', project, {'pro_name': 'theatre'}),
    url(r'^film/$', project, {'pro_name': 'film'}),
    url(r'^tv/$', project, {'pro_name': 'tv'}),
    url(r'^various/$', project, {'pro_name': 'various'}),
    url(r'^about/$', about),
    url(r'^Theatre/(?P<project_id>\d+)/$', project_details),
    url(r'^Film/(?P<project_id>\d+)/$', project_details),
    url(r'^Tv/(?P<project_id>\d+)/$', project_details),
    url(r'^Various/(?P<project_id>\d+)/$', project_details),
    url(r'^contact/$', contact),
    url(r'^links/$', links),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)

