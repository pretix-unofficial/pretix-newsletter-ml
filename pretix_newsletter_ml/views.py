import logging

from django import forms
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from i18nfield.forms import I18nFormField, I18nTextInput
from pretix.base.forms import SettingsForm
from pretix.base.models import Event
from pretix.control.views.event import (
    EventSettingsFormView, EventSettingsViewMixin,
)

logger = logging.getLogger(__name__)


class NewsletterSettingsForm(SettingsForm):
    newsletter_ml_subscribe_address = forms.EmailField(
        label=_("Subscribe address"),
        required=False,
    )
    newsletter_ml_add_automatically = forms.BooleanField(
        label=_("Add emails to the list without asking users in the frontend"),
        help_text=_("Not recommended, might be considered illegal/unfair business practice in your legislation."),
        required=False,
    )
    newsletter_ml_text = I18nFormField(
        label=_("Checkbox label"),
        required=True,
        widget=I18nTextInput,
    )


class MLSettings(EventSettingsViewMixin, EventSettingsFormView):
    model = Event
    form_class = NewsletterSettingsForm
    template_name = 'pretix_newsletter_ml/settings.html'
    permission = 'can_change_settings'

    def get_success_url(self) -> str:
        return reverse('plugins:pretix_newsletter_ml:settings', kwargs={
            'organizer': self.request.event.organizer.slug,
            'event': self.request.event.slug
        })
