# Ecommerce Backend

## Prerequisitos

1. Python >= 3.10
2. PostgreSQL >= 16.1
3. Internacionalización

- [Linux / Mac](https://www.gnu.org/software/gettext/)
- [Windows](https://mlocati.github.io/articles/gettext-iconv-windows.html)

```cmd
python manage.py makemessages -l en
```

- Nota: Reinicar el dispositivo

```cmd
python manage.py compilemessages -l en
```

## Requerimientos

### Opcional

1. Crear un venv

```cmd
python -m venv nombre_env
```

### Linux / Mac

Nota: Tener el venv activo si se creó previamente

```python
cd requirements
pip install -r linux.txt
```

### Windows

Nota: Tener el venv activo si se creó previamente

```python
cd requirements
pip install -r windows.txt
```

## Instalación

### Descargar el repositorio desde github

```github
https://github.com/sebasmd-projects/ecommerce_backend.git
```

## Descripción del proyecto

```plaintext
|   .gitignore
|   manage.py
|   README.md
|
+---apps
|   +---common
|   |   +---analytics
|   |   |   |   admin.py
|   |   |   |   apps.py
|   |   |   |   models.py
|   |   |   |   tests.py
|   |   |   |   urls.py
|   |   |   |   views.py
|   |   |   |   __init__.py
|   |   |   |
|   |   |   +---api
|   |   |   |       serializers.py
|   |   |   |       urls.py
|   |   |   |       views.py
|   |   |   |       __init__.py
|   |   |   |
|   |   |   \---migrations
|   |   |           __init__.py
|   |   |
|   |   +---locations
|   |   |   |   admin.py
|   |   |   |   apps.py
|   |   |   |   models.py
|   |   |   |   tests.py
|   |   |   |   urls.py
|   |   |   |   views.py
|   |   |   |   __init__.py
|   |   |   |
|   |   |   +---api
|   |   |   |       serializers.py
|   |   |   |       urls.py
|   |   |   |       views.py
|   |   |   |       __init__.py
|   |   |   |
|   |   |   +---locale
|   |   |   \---migrations
|   |   |           __init__.py
|   |   |
|   |   +---notifications
|   |   |   |   admin.py
|   |   |   |   apps.py
|   |   |   |   models.py
|   |   |   |   tests.py
|   |   |   |   urls.py
|   |   |   |   views.py
|   |   |   |   __init__.py
|   |   |   |
|   |   |   +---api
|   |   |   |       serializers.py
|   |   |   |       urls.py
|   |   |   |       views.py
|   |   |   |       __init__.py
|   |   |   |
|   |   |   +---locale
|   |   |   \---migrations
|   |   |           __init__.py
|   |   |
|   |   +---reports
|   |   |   |   admin.py
|   |   |   |   apps.py
|   |   |   |   models.py
|   |   |   |   tests.py
|   |   |   |   urls.py
|   |   |   |   views.py
|   |   |   |   __init__.py
|   |   |   |
|   |   |   +---api
|   |   |   |       serializers.py
|   |   |   |       urls.py
|   |   |   |       views.py
|   |   |   |       __init__.py
|   |   |   |
|   |   |   +---locale
|   |   |   \---migrations
|   |   |           __init__.py
|   |   |
|   |   +---support
|   |   |   |   admin.py
|   |   |   |   apps.py
|   |   |   |   models.py
|   |   |   |   tests.py
|   |   |   |   urls.py
|   |   |   |   views.py
|   |   |   |   __init__.py
|   |   |   |
|   |   |   +---api
|   |   |   |       serializers.py
|   |   |   |       urls.py
|   |   |   |       views.py
|   |   |   |       __init__.py
|   |   |   |
|   |   |   +---locale
|   |   |   \---migrations
|   |   |           __init__.py
|   |   |
|   |   +---users
|   |   |   |   admin.py
|   |   |   |   apps.py
|   |   |   |   models.py
|   |   |   |   tests.py
|   |   |   |   urls.py
|   |   |   |   views.py
|   |   |   |   __init__.py
|   |   |   |
|   |   |   +---api
|   |   |   |       filters.py
|   |   |   |       serializers.py
|   |   |   |       urls.py
|   |   |   |       views.py
|   |   |   |       __init__.py
|   |   |   |
|   |   |   \---migrations
|   |   |           __init__.py
|   |   |
|   |   \---utils
|   |       |   admin.py
|   |       |   apps.py
|   |       |   middleware.py
|   |       |   models.py
|   |       |   tests.py
|   |       |   urls.py
|   |       |   views.py
|   |       |   __init__.py
|   |       |
|   |       +---api
|   |       |       serializers.py
|   |       |       urls.py
|   |       |       views.py
|   |       |       __init__.py
|   |       |
|   |       +---backend
|   |       |       __init__.py
|   |       |
|   |       +---context_processors
|   |       |       __init__.py
|   |       |
|   |       +---data
|   |       |       skip_apps.txt
|   |       |       users.json
|   |       |
|   |       +---management
|   |       |   |   __init__.py
|   |       |   |
|   |       |   \---commands
|   |       |           delete_migrations.py
|   |       |           fill_users.py
|   |       |           startapi.py
|   |       |           __init__.py
|   |       |
|   |       +---migrations
|   |       |       __init__.py
|   |       |
|   |       \---templates
|   |           |   errors_template.html
|   |           |
|   |           \---registration
|   |                   login.html
|   |
|   \---ecommerce
|       +---billings
|       |   |   admin.py
|       |   |   apps.py
|       |   |   models.py
|       |   |   tests.py
|       |   |   urls.py
|       |   |   views.py
|       |   |   __init__.py
|       |   |
|       |   +---api
|       |   |       serializers.py
|       |   |       urls.py
|       |   |       views.py
|       |   |       __init__.py
|       |   |
|       |   \---migrations
|       |           __init__.py
|       |
|       +---checkouts
|       |   |   admin.py
|       |   |   apps.py
|       |   |   models.py
|       |   |   tests.py
|       |   |   urls.py
|       |   |   views.py
|       |   |   __init__.py
|       |   |
|       |   +---api
|       |   |       serializers.py
|       |   |       urls.py
|       |   |       views.py
|       |   |       __init__.py
|       |   |
|       |   \---migrations
|       |           __init__.py
|       |
|       +---comments
|       |   |   admin.py
|       |   |   apps.py
|       |   |   models.py
|       |   |   tests.py
|       |   |   urls.py
|       |   |   views.py
|       |   |   __init__.py
|       |   |
|       |   +---api
|       |   |       serializers.py
|       |   |       urls.py
|       |   |       views.py
|       |   |       __init__.py
|       |   |
|       |   \---migrations
|       |           __init__.py
|       |
|       +---discounts
|       |   |   admin.py
|       |   |   apps.py
|       |   |   models.py
|       |   |   tests.py
|       |   |   urls.py
|       |   |   views.py
|       |   |   __init__.py
|       |   |
|       |   +---api
|       |   |       serializers.py
|       |   |       urls.py
|       |   |       views.py
|       |   |       __init__.py
|       |   |
|       |   \---migrations
|       |           __init__.py
|       |
|       +---inventories
|       |   |   admin.py
|       |   |   apps.py
|       |   |   models.py
|       |   |   tests.py
|       |   |   urls.py
|       |   |   views.py
|       |   |   __init__.py
|       |   |
|       |   +---api
|       |   |       serializers.py
|       |   |       urls.py
|       |   |       views.py
|       |   |       __init__.py
|       |   |
|       |   \---migrations
|       |           __init__.py
|       |
|       +---orders
|       |   |   admin.py
|       |   |   apps.py
|       |   |   models.py
|       |   |   tests.py
|       |   |   urls.py
|       |   |   views.py
|       |   |   __init__.py
|       |   |
|       |   +---api
|       |   |       serializers.py
|       |   |       urls.py
|       |   |       views.py
|       |   |       __init__.py
|       |   |
|       |   \---migrations
|       |           __init__.py
|       |
|       +---payments
|       |   |   admin.py
|       |   |   apps.py
|       |   |   models.py
|       |   |   tests.py
|       |   |   urls.py
|       |   |   views.py
|       |   |   __init__.py
|       |   |
|       |   +---api
|       |   |       serializers.py
|       |   |       urls.py
|       |   |       views.py
|       |   |       __init__.py
|       |   |
|       |   \---migrations
|       |           __init__.py
|       |
|       +---products
|       |   |   admin.py
|       |   |   apps.py
|       |   |   models.py
|       |   |   tests.py
|       |   |   urls.py
|       |   |   views.py
|       |   |   __init__.py
|       |   |
|       |   +---api
|       |   |       serializers.py
|       |   |       urls.py
|       |   |       views.py
|       |   |       __init__.py
|       |   |
|       |   \---migrations
|       |           __init__.py
|       |
|       +---ratings
|       |   |   admin.py
|       |   |   apps.py
|       |   |   models.py
|       |   |   tests.py
|       |   |   urls.py
|       |   |   views.py
|       |   |   __init__.py
|       |   |
|       |   +---api
|       |   |       serializers.py
|       |   |       urls.py
|       |   |       views.py
|       |   |       __init__.py
|       |   |
|       |   \---migrations
|       |           __init__.py
|       |
|       +---reviews
|       |   |   admin.py
|       |   |   apps.py
|       |   |   models.py
|       |   |   tests.py
|       |   |   urls.py
|       |   |   views.py
|       |   |   __init__.py
|       |   |
|       |   +---api
|       |   |       serializers.py
|       |   |       urls.py
|       |   |       views.py
|       |   |       __init__.py
|       |   |
|       |   \---migrations
|       |           __init__.py
|       |
|       +---shippings
|       |   |   admin.py
|       |   |   apps.py
|       |   |   models.py
|       |   |   tests.py
|       |   |   urls.py
|       |   |   views.py
|       |   |   __init__.py
|       |   |
|       |   +---api
|       |   |       serializers.py
|       |   |       urls.py
|       |   |       views.py
|       |   |       __init__.py
|       |   |
|       |   \---migrations
|       |           __init__.py
|       |
|       \---shoppingcarts
|           |   admin.py
|           |   apps.py
|           |   models.py
|           |   tests.py
|           |   urls.py
|           |   views.py
|           |   __init__.py
|           |
|           +---api
|           |       serializers.py
|           |       urls.py
|           |       views.py
|           |       __init__.py
|           |
|           \---migrations
|                   __init__.py
|
+---app_core
|   |   asgi.py
|   |   settings.py
|   |   urls.py
|   |   urls_custom.py
|   |   __init__.py
|   |
|   +---settings_config
|   |       settings_apps.py
|   |       settings_locale_paths.py
|   |       settings_middleware.py
|   |       settings_rest.py
|   |       __init__.py
|   |
|   \---static
|           favicon.ico
|
\---requirements
        linux.txt
        windows.txt
```

## Versiones

- 0.0.X: Se incrementa cuando se realizan correcciones de errores o pequeñas mejoras que no afectan la compatibilidad con versiones anteriores.
- 0.X.0: Se incrementa cuando se añade una nueva carácteristica o un cambio significativo.
- X.0.0: Se incrementa cuando hay una versión estable del proyecto.

### v0.0.1

- .gitignore
- manage.py: se inicializa el servidor de desarrollo en 0.0.0.0:8000
- README.md: creación del archivo
- settings.py: configuración personalizada y uso de .env
- urls.py: customización del archivo urls para gestionar las del proyecto, de terceros e internacionalización
- apps/common: aplicaciones comúnes
- apps/ecommerce: aplicaciones propias de un ecommerce
- requerimientos: se definen las dependencias para los SO linux/mac y Windows
- apps.common.utils.models: modelo generico del cual hereden la mayoria y registro de uso de los endpoints
- apps.common.utils: aplicación que maneja lo camandos y entre otras utilidades
- apps.common.users: aplicación para la gestión completa de usuarios (quienes usen la aplicación, incluye roles y otras funcionalidades)
