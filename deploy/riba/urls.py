from django.conf.urls import include, url
from django.contrib import admin
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
from riba.views import ChatterBotAppView


urlpatterns = [
    url(r'^$', ChatterBotAppView.as_view(), name='main'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^chatterbot/', include('chatterbot.ext.django_chatterbot.urls', namespace='chatterbot')),
    url(r'^appointment.html', appointment.as_view(), name='appointment'),
    url(r'^contact.html', contact.as_view(), name='contact'),
    url(r'^doctor.html', doctor.as_view(), name='doctor'),
]
