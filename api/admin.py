from django.contrib import admin
from api.models import Plantilla, Seccion, TipoDeDato, Pregunta, Programa

### CREDENCIALES DEL ADMIN
### username = inspi
### password = inspiadmin

admin.site.register(Plantilla)
admin.site.register(Seccion)
admin.site.register(TipoDeDato)
admin.site.register(Pregunta)
admin.site.register(Programa)