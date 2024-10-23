from django.urls import path
from . import views  # Importar las vistas desde el archivo views.py

urlpatterns = [
    # Página de inicio
    path('', views.index, name='index'),

    # Lista de proyectos
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),

    # Lista de tareas de un proyecto específico
    path('proyectos/<int:proyecto_id>/tareas/', views.lista_tareas_proyecto, name='lista_tareas_proyecto'),

    # Lista de usuarios asignados a una tarea específica
    path('tareas/<int:tarea_id>/usuarios-asignados/', views.usuarios_asignados_tarea, name='usuarios_asignados_tarea'),

    # Tareas con observaciones
    path('tareas/observaciones/', views.tareas_con_observaciones, name='tareas_con_observaciones'),

    # Tareas completadas entre dos años
    path('tareas/completadas/', views.tareas_completadas_por_anio, name='tareas_completadas_por_anio'),

    # Último comentario en una tarea de un proyecto específico
    path('proyectos/<int:proyecto_id>/ultimo-comentario/', views.ultimo_comentario_tarea_proyecto, name='ultimo_comentario_tarea_proyecto'),

    # Comentarios por palabra clave y año específico
    path('comentarios/', views.comentarios_por_palabra_y_anio, name='comentarios_por_palabra_y_anio'),

    # Etiquetas de un proyecto específico
    path('proyectos/<int:proyecto_id>/etiquetas/', views.etiquetas_de_proyecto, name='etiquetas_de_proyecto'),

    # Usuarios sin tarea asignada
    path('usuarios/sin-tarea/', views.usuarios_sin_tarea, name='usuarios_sin_tarea'),
]
