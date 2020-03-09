from django import forms
from django.dispatch import receiver
from django.urls import resolve, reverse
from django.utils.translation import gettext_lazy as _, gettext_noop
from i18nfield.strings import LazyI18nString
from pretix.base.settings import settings_hierarkey
from pretix.base.signals import logentry_display, order_placed
from pretix.base.templatetags.rich_text import rich_text_snippet
from pretix.control.signals import nav_event_settings
from pretix.presale.signals import contact_form_fields

from .tasks import newsletter_ml_order_placed


@receiver(nav_event_settings, dispatch_uid='newsletter_ml_nav')
def navbar_info(sender, request, **kwargs):
    url = resolve(request.path_info)
    if not request.user.has_event_permission(request.organizer, request.event, 'can_change_event_settings', request=request):
        return []
    return [{
        'label': _('Mailing list'),
        'icon': 'envelope-open',
        'url': reverse('plugins:pretix_newsletter_ml:settings', kwargs={
            'event': request.event.slug,
            'organizer': request.organizer.slug,
        }),
        'active': url.namespace == 'plugins:pretix_newsletter_ml',
    }]


@receiver(order_placed, dispatch_uid='newsletter_ml_order_placed')
def order_placed(sender, order, **kwargs):
    skip = (
        not sender.settings.newsletter_ml_subscribe_address or (
            not sender.settings.newsletter_ml_add_automatically
            and not order.meta_info_data.get('contact_form_data', {}).get('ml_newsletter') is True
        )
    )
    if skip:
        return

    newsletter_ml_order_placed.apply_async(args=(sender.pk, order.pk))


@receiver(contact_form_fields, dispatch_uid='newsletter_ml_contact_form_fields')
def cf_formfields(sender, **kwargs):
    skip = (
        not sender.settings.newsletter_ml_subscribe_address or
        sender.settings.newsletter_ml_add_automatically
    )
    if skip:
        return {}
    return {
        'ml_newsletter': forms.BooleanField(
            label=rich_text_snippet(sender.settings.newsletter_ml_text),
            required=False,
        )
    }


@receiver(signal=logentry_display, dispatch_uid="newsletter_ml_logentry_display")
def pretixcontrol_logentry_display(sender, logentry, **kwargs):
    if not logentry.action_type.startswith('pretix_newsletter_ml'):
        return

    plains = {
        'pretix_newsletter_ml.subscribe': _("A subscribe request for the mailing list has been sent."),
    }

    if logentry.action_type in plains:
        return plains[logentry.action_type]


settings_hierarkey.add_default('newsletter_ml_text', LazyI18nString.from_gettext(gettext_noop(
    "Yes, I want to receive the organizer's newsletter"
)), LazyI18nString)
