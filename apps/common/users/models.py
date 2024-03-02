import uuid
from datetime import date

from auditlog.registry import auditlog
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField, UUIDField
from django.utils.translation import gettext_lazy as _

from ..utils.models import TimeStampedModel


class UserModel(TimeStampedModel, AbstractUser):
    id = UUIDField(
        'ID',
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        serialize=False,
        editable=False
    )

    cell_phone = CharField(
        _('teléfono'),
        max_length=15,
        null=True,
        blank=True
    )

    birthday = DateField(
        _('fecha de nacimiento'),
        default=date.today,
        blank=True,
        null=True
    )

    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name'
    ]

    def get_age(self):
        return date.today().year - self.birthday.year - (
            (date.today().month, date.today().day) < (
                self.birthday.month, self.birthday.day)
        )

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        self.username = self.username.lower()

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.get_full_name()

    class Meta:
        db_table = 'apps_user'
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')


auditlog.register(
    UserModel,
    serialize_data=True
)
