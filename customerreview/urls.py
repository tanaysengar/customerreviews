from django.conf.urls import patterns, include, url

from django.contrib import admin

from fileupload.views import list

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'customerreview1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/', 'fileupload.views.list', name='list'),
    url(r'^list_upc/', 'main.views.list_upc', name='list_upc'),

)
