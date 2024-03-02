from datetime import datetime

from django.conf import settings
from django.db import transaction
from django.utils.translation import gettext as _

from .models import RequestLogModel


class APILogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request_log = None

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith('/api/') and request.path not in settings.MIDDLEWARE_NOT_INCLUDE:
            self.request_log = RequestLogModel.get_instance()
            self.save_request_log(request, response)
        return response

    def save_request_log(self, request, response):
        client_ip = self.get_client_ip(request)
        referring_page = request.META.get('HTTP_REFERER', '')
        origin = request.META.get('HTTP_ORIGIN', '')
        entry = {
            _('marca_de_tiempo'): datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            _('metodo'): request.method,
            _('url'): request.path,
            _('estado'): response.status_code,
            _('ip_cliente'): client_ip,
            _('pagina_de_referencia'): referring_page,
            _('origen'): origin,
        }
        with transaction.atomic():
            self.request_log.add_request_entry(entry)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
