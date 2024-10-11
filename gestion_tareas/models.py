from django.db import models
from django.utils import timezone


# Modelo Usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre


# Modelo Proyecto
class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='proyectos_creados')

    usuarios_asignados = models.ManyToManyField(Usuario, related_name='proyectos_asignados', blank=True)

    def __str__(self):
        return self.nombre


# Modelo Etiqueta
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre


# Modelo Tarea
class Tarea(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'PE', 'Pendiente'
        PROGRESO = 'PR', 'Progreso'
        COMPLETADA = 'CO', 'Completada'

    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    estado = models.CharField(max_length=10, choices=Estado.choices, default=Estado.PENDIENTE)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateField(default=timezone.now)
    hora_vencimiento = models.DateTimeField(default=timezone.now)

    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas_creadas')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    etiquetas_asociadas = models.ManyToManyField(Etiqueta, related_name='tareas')

    def __str__(self):
        return self.titulo


# Modelo Asignación de Tarea (Tabla intermedia para asignar usuarios a tareas)
class AsignacionTareas(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True)
    fecha_asignacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Asignación de {self.usuario} a {self.tarea}'


# Modelo Comentario
class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self):
        return f'Comentario de {self.autor} en {self.tarea}'
