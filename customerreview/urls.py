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
    url(r'^list_sites/', 'main.views.list_sites', name='list_sites'),
    url(r'^upc_reviews/(?P<code>\w{0,50})/$', 'main.views.upc_reviews', name='upc_reviews'),
    url(r'^add_review', 'main.views.add_review', name='add_review'),
)
