from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from eleni_app.views import home_page 
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', home_page),
    #url(r'^home/$', home_page),
    #url(r'^theatre/$', theatre),
    #url(r'^snippets/$', views.SnippetList.as_view()),
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.Snippet_Detail.as_view()),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('eleni_app.urls', namespace="eleni_app")),
    #url(r'^contact/$', 'contact.views.contact', name='contact'),
    #url(r'^thanks/$', 'contact.views.thanks', name='thanks'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
) 