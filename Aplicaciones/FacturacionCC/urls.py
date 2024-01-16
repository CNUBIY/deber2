from django.urls import path
from . import views

urlpatterns=[
    path('',views.listadoDetalles),
    path('guardarDetalle/',views.guardarDetalle),
    path('eliminarDetalle/<id_cc>',views.eliminarDetalle),
    path('editarDetalle/<id_cc>', views.editarDetalle, name='editarDetalle'),
    path('procesarActualizacionDetalle/<id_cc>', views.procesarActualizacionDetalle, name='procesarActualizacionDetalle'),





    path('listadoProvincias/',views.listadoProvincias),
    path('guardarProvincia/',views.guardarProvincia),
    path('eliminarProvincia/<id_cc>',views.eliminarProvincia),
    path('editarProvincia/<id_cc>', views.editarProvincia, name='editarProvincia'),
    path('procesarActualizacionProvincia/<id_cc>', views.procesarActualizacionProvincia, name='procesarActualizacionProvincia'),


    path('listadoTipos/',views.listadoTipos),
    path('guardarTipo/',views.guardarTipo),
    path('eliminarTipo/<id_cc>',views.eliminarTipo),
    path('editarTipo/<id_cc>', views.editarTipo, name='editarTipo'),
    path('procesarActualizacionTipo/<id_cc>', views.procesarActualizacionTipo, name='procesarActualizacionTipo'),


    path('listadoIngredientes/',views.listadoIngredientes),
    path('guardarIngrediente/',views.guardarIngrediente),
    path('eliminarIngrediente/<id_cc>',views.eliminarIngrediente),
    path('editarIngrediente/<id_cc>', views.editarIngrediente, name='editarIngrediente'),
    path('procesarActualizacionIngrediente/<id_cc>', views.procesarActualizacionIngrediente, name='procesarActualizacionIngrediente'),



    path('listadoClientes/',views.listadoClientes),
    path('guardarCliente/',views.guardarCliente),
    path('eliminarCliente/<id_cc>',views.eliminarCliente),
    path('editarCliente/<id_cc>', views.editarCliente, name='editarCliente'),
    path('procesarActualizacionCliente/<id_cc>', views.procesarActualizacionCliente, name='procesarActualizacionCliente'),



    path('listadoPedidos/',views.listadoPedidos),
    path('guardarPedido/',views.guardarPedido),
    path('eliminarPedido/<id_cc>',views.eliminarPedido),
    path('editarPedido/<id_cc>', views.editarPedido, name='editarPedido'),
    path('procesarActualizacionPedido/<id_cc>', views.procesarActualizacionPedido, name='procesarActualizacionPedido'),


    path('listadoPlatillos/',views.listadoPlatillos),
    path('guardarPlatillo/',views.guardarPlatillo),
    path('eliminarPlatillo/<id_cc>',views.eliminarPlatillo),
    path('editarPlatillo/<id_cc>', views.editarPlatillo, name='editarPlatillo'),
    path('procesarActualizacionPlatillo/<id_cc>', views.procesarActualizacionPlatillo, name='procesarActualizacionPlatillo'),



    path('listadoRecetas/',views.listadoRecetas),
    path('guardarReceta/',views.guardarReceta),
    path('eliminarReceta/<id_cc>',views.eliminarReceta),
    path('editarReceta/<id_cc>', views.editarReceta, name='editarReceta'),
    path('procesarActualizacionReceta/<id_cc>', views.procesarActualizacionReceta, name='procesarActualizacionReceta'),



    path('reportes/',views.reportes)
]
