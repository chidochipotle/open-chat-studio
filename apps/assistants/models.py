from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from field_audit import audit_fields
from field_audit.models import AuditingManager

from apps.teams.models import BaseTeamModel
from apps.utils.models import BaseModel


class OpenAiAssistantManager(AuditingManager):
    pass


@audit_fields(
    "assistant_id",
    "name",
    "instructions",
    "builtin_tools",
    "llm_provider",
    "llm_model",
    audit_special_queryset_writes=True,
)
class OpenAiAssistant(BaseTeamModel):
    assistant_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    instructions = models.TextField()
    builtin_tools = ArrayField(models.CharField(max_length=128), default=list)
    llm_provider = models.ForeignKey(
        "service_providers.LlmProvider",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="LLM Provider",
    )
    llm_model = models.CharField(
        max_length=255,
        help_text="The LLM model to use.",
        verbose_name="LLM Model",
    )

    objects = OpenAiAssistantManager()

    def get_absolute_url(self):
        return reverse("assistants:edit", args=[self.team.slug, self.id])