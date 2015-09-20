from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

import vp.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', vp.views.index, name='index'),

    # Authentication
    url(r'^login/$', vp.views.login_view, name='login'),
    url(r'^logout/$', vp.views.logout_user, name='logout'),
    url(r'^register/$', vp.views.register_view, name='register'),
    url(r'^authenticate_user/$', vp.views.authenticate_user, name='authenticate_user'),

    # Location entry map
    url(r'^mapview/$', vp.views.map_view, name='map_view'),
    url(r'^edit_location/(?P<location_id>[0-9]+)/$', vp.views.location_editor_view, name='location_editor'),

    # Admin
    url(r'^admin/', include(admin.site.urls))
)