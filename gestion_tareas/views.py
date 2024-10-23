from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def index(request):
    return render(request, 'gestion_tareas/index.html')



def lista_proyectos(request):
    proyectos = Proyecto.objects.select_related().prefetch_related();
    return render(request, 'gestion_tareas/proyectos.html', {'proyectos': proyectos})


# Lista de tareas de un proyecto específico
def lista_tareas_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto.objects.prefetch_related('tareas__comentarios'), id=proyecto_id)  # Pre-cargar tareas y comentarios
    tareas = proyecto.tareas.all().order_by('-fecha_creacion')
    return render(request, 'gestion_tareas/tareas_proyecto.html', {'proyecto': proyecto, 'tareas': tareas})

# Lista de usuarios asignados a una tarea
def usuarios_asignados_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea.objects.prefetch_related('asignaciontareas__usuario'), id=tarea_id)  # Pre-cargar asignaciones y usuarios
    asignaciones = tarea.asignaciontareas.all().order_by('fecha_asignacion')
    usuarios_asignados = [asignacion.usuario for asignacion in asignaciones]
    return render(request, 'gestion_tareas/usuarios_asignados_tarea.html', {'tarea': tarea, 'usuarios_asignados': usuarios_asignados})

# Tareas con observaciones
def tareas_con_observaciones(request):
    # Si no tienes un related_name definido, usa 'asignaciontareas_set'
    tareas = Tarea.objects.filter(asignaciontareas__observaciones__isnull=False).distinct().prefetch_related('asignaciontareas_set')  
    return render(request, 'gestion_tareas/tareas_observaciones.html', {'tareas': tareas})


# Tareas completadas entre dos años
def tareas_completadas_por_anio(request):
    anio_inicio = request.GET.get('anio_inicio', 2020)
    anio_fin = request.GET.get('anio_fin', 2023)
    tareas = Tarea.objects.filter(fecha_creacion__year__gte=anio_inicio, fecha_creacion__year__lte=anio_fin, estado=Tarea.Estado.COMPLETADA).select_related('proyecto')  # Pre-cargar proyecto
    return render(request, 'gestion_tareas/tareas_completadas.html', {'tareas': tareas})

# Último comentario en una tarea de un proyecto
def ultimo_comentario_tarea_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto.objects.prefetch_related('tareas__comentarios'), id=proyecto_id)  # Pre-cargar tareas y comentarios
    ultimo_comentarios = {}

    for tarea in proyecto.tareas.all():
        ultimo_comentario = tarea.comentarios.order_by('-fecha_comentario').first()
        if ultimo_comentario:
            ultimo_comentarios[tarea] = ultimo_comentario

    return render(request, 'gestion_tareas/ultimo_comentario.html', {'proyecto': proyecto, 'ultimo_comentarios': ultimo_comentarios})

# Comentarios por palabra clave y año específico
def comentarios_por_palabra_y_anio(request):
    palabra_clave = request.GET.get('palabra', '')
    anio = request.GET.get('anio', 2024)
    comentarios = Comentario.objects.filter(contenido__icontains=palabra_clave, fecha_comentario__year=anio).select_related('autor')  # Pre-cargar usuario
    return render(request, 'gestion_tareas/comentarios_por_palabra.html', {'comentarios': comentarios})

# Etiquetas de un proyecto
def etiquetas_de_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto.objects.prefetch_related('tareas__etiquetas'), id=proyecto_id)  # Pre-cargar tareas y etiquetas
    etiquetas = Etiqueta.objects.filter(tareas__proyecto=proyecto).distinct()
    return render(request, 'gestion_tareas/etiquetas_proyecto.html', {'proyecto': proyecto, 'etiquetas': etiquetas})

# Usuarios sin tarea asignada
def usuarios_sin_tarea(request):
    usuarios = Usuario.objects.exclude(tareas_creadas__isnull=False).distinct().prefetch_related('tareas_creadas')  # Pre-cargar tareas
    return render(request, 'gestion_tareas/usuarios_sin_tarea.html', {'usuarios': usuarios})

