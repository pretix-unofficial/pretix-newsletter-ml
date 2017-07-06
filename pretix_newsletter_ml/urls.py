from django.conf.urls import url

from .views import MLSettings

urlpatterns = [
    url(r'^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/newsletter_ml/settings$',
        MLSettings.as_view(), name='settings'),
]
