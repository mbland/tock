from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from hours.views import WeekListView, TimecardCreateView, TimecardUpdateView

urlpatterns = patterns('',
    url(r'^$', WeekListView.as_view(), name='ListWeeks'),
    url(r'^timesheet/create/(?P<week>[\w-]+)/$', TimecardCreateView.as_view(success_url='/'), name='CreateTimesheet'),
    url(r'^timesheet/update/(?P<week>[\w-]+)/$', TimecardUpdateView.as_view(success_url='/'), name='UpdateTimesheet'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)