import functools
from enum import Enum

from django import forms
from django.db.models import Field

from apps.generics.type_select_form import TypeSelectForm

from . import const
from .models import LlmProvider, LlmProviderType, VoiceProvider, VoiceProviderType
from .tables import LlmProviderTable, VoiceProviderTable


class ServiceProvider(Enum):
    llm = const.LLM
    voice = const.VOICE

    @property
    def model(self):
        match self:
            case ServiceProvider.llm:
                return LlmProvider
            case ServiceProvider.voice:
                return VoiceProvider
        raise ValueError(f"Invalid provider type: {self}")

    @property
    def table(self):
        match self:
            case ServiceProvider.llm:
                return LlmProviderTable
            case ServiceProvider.voice:
                return VoiceProviderTable
        raise ValueError(f"Invalid provider type: {self}")

    @property
    def subtype(self):
        """Return the enum for the subtypes of this provider type.

        It is required that the enum has a `form_cls` property which returns
        the config form class for that subtype."""
        match self:
            case ServiceProvider.llm:
                return LlmProviderType
            case ServiceProvider.voice:
                return VoiceProviderType
        raise ValueError(f"Invalid provider type: {self}")

    @property
    def primary_fields(self):
        """The fields on the model which should be included in the main form."""
        return ["name", "type"]

    @property
    def provider_type_field(self):
        """The name of the model field which determines the provider type."""
        return "type"

    def get_form_initial(self, instance):
        """Return the initial data for the config form."""
        return instance.config


def get_service_provider_config_form(provider: ServiceProvider, data=None, instance=None) -> TypeSelectForm:
    """Return the form for the service provider. This is a 'type select form' which will include the main form
    and the config form for the selected provider type.
    """
    initial_config = provider.get_form_initial(instance) if instance else None
    return TypeSelectForm(
        primary=_get_main_form(provider, data=data.copy() if data else None, instance=instance),
        secondary={
            subtype: subtype.form_cls(data=data.copy() if data else None, initial=initial_config)
            for subtype in provider.subtype
        },
        secondary_key_field=provider.provider_type_field,
    )


def _get_main_form(provider: ServiceProvider, instance=None, data=None):
    """Get the main 'model form' for the service provider which will be used to create the model instance."""
    form_cls = forms.modelform_factory(
        provider.model,
        fields=provider.primary_fields,
        formfield_callback=functools.partial(formfield_for_dbfield, provider=provider),
    )
    form = form_cls(data=data, instance=instance)
    if instance:
        form.fields[provider.provider_type_field].disabled = True

    return form


def formfield_for_dbfield(db_field: Field, provider: ServiceProvider, **kwargs):
    """This is a callback function used by Django's `modelform_factory` to create the form fields for the model.
    It's use here is to customize the `provider_type` field."""
    if db_field.name == provider.provider_type_field:
        # remove 'empty' value from choices
        return forms.TypedChoiceField(empty_value=None, choices=provider.subtype.choices)
    return db_field.formfield(**kwargs)