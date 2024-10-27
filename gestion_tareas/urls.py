from django.urls import path
from . import views  # Importar las vistas desde el archivo views.py

urlpatterns = [
    # Página de inicio
    path('', views.index, name='index'),
    
    # Lista de proyectos
    path('proyectos', views.lista_proyectos, name='lista_proyectos'),
    
    # Lista de tareas de un proyecto específico
    path('proyectos/<int:proyecto_id>/tareas/', views.lista_tareas_proyecto, name='lista_tareas_proyecto'),

    # Lista de usuarios asignados a una tarea
    path('tareas/<int:tarea_id>/usuarios_asignados/', views.lista_usuarios_asignados_tarea, name='lista_usuarios_asignados'),


    # Tarea con observaciones con texto
    path('tareas/observacion/<str:texto_observacion>/', views.tareas_por_observacion, name='tareas_por_observacion'),

    # Tarea completadas por años
    path('tareas/completadas/<int:anio_inicio>/<int:anio_fin>/', views.tareas_completadas_por_anio, name='tareas_completadas_por_anio'),


    # Último cmentario tarea de proyectos
    path('proyecto/<int:proyecto_id>/ultimo-comentario/', views.ultimo_usuario_comentario, name='ultimo_usuario_comentario'),


    # comentario de tarea filtrado por palabra y fecha
    path('tarea/<int:tarea_id>/comentarios/<str:palabra_inicial>/<int:anio>/', views.comentarios_por_palabra_y_ano, name='comentarios_por_palabra_y_ano'),

    # etiquetas del proyecto
    path('proyecto/<int:proyecto_id>/etiquetas/', views.etiquetas_del_proyecto, name='etiquetas_del_proyecto'),

    # usuarios no asignados
    path('tarea/<int:tarea_id>/usuarios-no-asignados/', views.usuarios_no_asignados_a_tarea, name='usuarios_no_asignados_a_tarea'),
    

]















"""
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
"""