from django.contrib import admin

from .models import PQaror
from .models_vazir import VQaror
from .models_hokim import HQaror

admin.site.register(PQaror)
admin.site.register(VQaror)
admin.site.register(HQaror)