from django.shortcuts import render, get_object_or_404
from .models import *



# Desde una página de Inicio debe poder acceder a todas las URLs que se indiquen.
def index(request):
    return render(request, 'gestion_tareas/index.html')


# Crea una URL que muestre una lista de todos los proyectos de la aplicación con sus datos correspondientes.

def lista_proyectos(request):
    proyectos = Proyecto.objects.select_related("creador").prefetch_related('usuarios_asignados')
    return render(request, 'gestion_tareas/proyectos.html', {'proyectos': proyectos})


# Crear una URL que muestre todas las tareas que están asociadas a un proyecto, ordenadas por fecha de creación descendente.
def lista_tareas_proyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)  
    tareas = Tarea.objects.filter(proyecto=proyecto).order_by('-fecha_creacion')  
    
    return render(request, 'gestion_tareas/tareas_proyecto.html', {'tareas': tareas, 'proyecto': proyecto})


#Crear una URL que muestre todos los usuarios que están asignados a una tarea ordenados por la fecha de asignación de la tarea de forma ascendente. 
def lista_usuarios_asignados_tarea(request, tarea_id):
    # Obtiene la tarea específica o lanza un 404 si no se encuentra
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    # Obtiene los usuarios asignados a la tarea a través de la relación ManyToMany
    usuarios_asignados = tarea.usuarios_asignados.all()

           
    return render(request, 'gestion_tareas/usuarios_asignados.html', {
        'tarea': tarea,
        'usuarios_asignados': usuarios_asignados
    })


def tareas_por_observacion(request, texto_observacion):
    asignaciones = AsignacionTareas.objects.filter(observaciones__icontains=texto_observacion)
    
    # Extraemos así las tareas relacionadas con estas asignaciones
    tareas = [asignacion.tarea for asignacion in asignaciones]

    return render(request, 'gestion_tareas/tareas_por_observacion.html', {'tareas': tareas, 'texto_observacion': texto_observacion})


#Crear una URL que muestre todos las tareas que se han creado entre dos años y el estado sea “Completada”.
# views.py
from django.shortcuts import render
from .models import Tarea

def tareas_completadas_por_anio(request, anio_inicio, anio_fin):
    # Filtra las tareas entre las fechas especificadas y con estado "Completada"
    tareas = Tarea.objects.filter(fecha_creacion__year__gte=anio_inicio, fecha_creacion__year__lte=anio_fin, estado=Tarea.Estado.COMPLETADA
)

    return render(request, 'gestion_tareas/tareas_completadas_anio.html', {'tareas': tareas, 'anio_inicio': anio_inicio, 'anio_fin': anio_fin})



#Crear una URL que obtenga el último usuario que ha comentado en una tarea de un proyecto en concreto.
def ultimo_usuario_comentario(request, proyecto_id):
    

    ultimo_comentario_info = Comentario.objects.filter(tarea__proyecto_id=proyecto_id) .order_by('-fecha_comentario').values('autor__nombre', 'tarea__titulo')[:1]
    
   
    return render(request, 'gestion_tareas/ultimo_comentario.html', {'ultimo_comentario_info': ultimo_comentario_info})



#Crear una URL que obtenga todos los comentarios de una tarea que empiecen por la palabra que se pase en la URL y que el año del comentario sea uno en concreto.

def comentarios_por_palabra_y_ano(request, tarea_id, palabra_inicial, anio):

    comentarios = Comentario.objects.filter(tarea_id=tarea_id, contenido__startswith=palabra_inicial, fecha_comentario__year=anio)

    return render(request, 'gestion_tareas/comentarios_por_palabra_y_anio.html', {'comentarios': comentarios, 'palabra_inicial': palabra_inicial, 'anio': anio})



#Crear una URL que obtenga todas las etiquetas que se han usado en todas las tareas de un proyecto.
def etiquetas_del_proyecto(request, proyecto_id):
  
    proyecto = Proyecto.objects.get(id=proyecto_id)


    etiquetas = Etiqueta.objects.filter(tareas__proyecto=proyecto).distinct().all()

    return render(request, 'gestion_tareas/etiquetas_proyecto.html', {
        'proyecto': proyecto, 
        'etiquetas': etiquetas
    })

#Crear una URL que muestre todos los usuarios que no están asignados a una tarea.
def usuarios_no_asignados_a_tarea(request, tarea_id):
   
    tarea = get_object_or_404(Tarea, id=tarea_id) # gestionamos una posible id no valida para devolver el error 404

   
    usuarios_asignados = AsignacionTareas.objects.filter(tarea=tarea).values_list('usuario', flat=True)
    usuarios_no_asignados = Usuario.objects.exclude(id__in=usuarios_asignados)

    return render(request, 'gestion_tareas/usuarios_no_asignados.html', {
        'tarea': tarea,
        'usuarios_no_asignados': usuarios_no_asignados
    })


#Crear una página de Error personalizada para cada uno de los 4 tipos de errores que pueden ocurrir en nuestra Web.
def error_400(request, exception=None):
    return render(request, 'errores/400.html', status=400)

def error_403(request, exception=None):
    return render(request, 'errores/403.html', status=403)

def error_404(request, exception=None):
    return render(request, 'errores/404.html', status=404)

def error_500(request):
    return render(request, 'errores/500.html', status=500)
