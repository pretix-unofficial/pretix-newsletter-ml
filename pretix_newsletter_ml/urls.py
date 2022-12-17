from django.urls import path

from .views import MLSettings

urlpatterns = [
    path('control/event/<str:organizer>/<str:event>/newsletter_ml/settings',
        MLSettings.as_view(), name='settings'),
]
