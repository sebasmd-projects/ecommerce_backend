from auditlog.models import AuditlogHistoryField
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

utils_path: str = settings.UTILS_PATH
utils_db_name = utils_path.replace('.', '_')


class TimeStampedModel(models.Model):
    history = AuditlogHistoryField()

    language = models.CharField(
        _("idioma"),
        max_length=50
    )

    created = models.DateTimeField(
        _('creado'),
        default=timezone.now
    )

    updated = models.DateTimeField(
        _('actualizado'),
        auto_now=True
    )

    is_active = models.BooleanField(
        _("activo"),
        default=True
    )

    default_order = models.PositiveIntegerField(
        _('prioridad'),
        default=1,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True

class RequestLogModel(TimeStampedModel):
    requests = models.JSONField(
        _("peticiones"),
        blank=True,
        null=True,
        default=dict
    )

    @classmethod
    def get_instance(cls):
        instance, _ = cls.objects.get_or_create(id=1)
        return instance

    def add_request_entry(self, entry):
        requests = self.requests or []
        requests.insert(0, entry)
        self.requests = requests
        self.save()

    def __str__(self) -> str:
        return f'{self.id}'

    class Meta:
        db_table = f'{utils_db_name}_requestlog'
        verbose_name = _('Registro')
        verbose_name_plural = _('Registros')
