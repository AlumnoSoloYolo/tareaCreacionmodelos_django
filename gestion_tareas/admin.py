from django.contrib import admin
from .models import Usuario, Proyecto, Tarea, Etiqueta, Comentario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Proyecto)
admin.site.register(Tarea)
admin.site.register(Etiqueta)
admin.site.register(Comentario)
