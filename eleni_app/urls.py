from django.conf.urls import patterns, include, url
from django.conf import settings
#from django.conf.urls.static import static
from eleni_app.views import home_page, project, project_details, about, contact, thanks, enter, eleni, links
#from rest_framework.urlpatterns import format_suffix_patterns
#from django.conf.urls.static import static
#from django.contrib import admin
#admin.autodiscover()

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
    url(r'^thanks/$', thanks),
    url(r'^links/$', links),
    #url(r'^snippets/$', views.SnippetList.as_view()),
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.Snippet_Detail.as_view()),
    # url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    #url(r'^admin/', include(admin.site.urls)),
) #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns = format_suffix_patterns(urlpatterns)
