from django.shortcuts import render, redirect
from .models import Cliente, Tipo, Ingrediente, Detalle, Receta, Provincia, Pedido, Platillo
from django.contrib import messages
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Create your views here.

#PROVINCIAS

def listadoProvincias(request):
    provinciaBdd=Provincia.objects.all()
    return render(request,'listadoProvincias.html',{'provincias':provinciaBdd})

def guardarProvincia(request):
    nombre_cc=request.POST["nombre_cc"]
    codigo_cc=request.POST["codigo_cc"]
    foto_cc=request.FILES.get("foto_cc")

    nuevoProvincia = Provincia.objects.create(
        nombre_cc=nombre_cc,
        codigo_cc=codigo_cc,
        foto_cc=foto_cc,
    )

    messages.success(request, 'Provincia guardada exitosamente')
    return redirect('/listadoProvincias')


def eliminarProvincia(request,id_cc):
    eliminarProvincia=Provincia.objects.get(id_cc=id_cc)
    eliminarProvincia.delete()
    return redirect('/listadoProvincias')

def editarProvincia(request, id_cc):
    provinciaEditar = Provincia.objects.get(id_cc=id_cc)
    return render(request, 'editarProvincia.html', {'provincia': provinciaEditar})


def procesarActualizacionProvincia(request, id_cc):
    id_cc = request.POST["id_cc"]
    nombre_cc = request.POST["nombre_cc"]
    codigo_cc = request.POST["codigo_cc"]
    foto_cc=request.FILES.get("foto_cc")

    provinciaEditar = Provincia.objects.get(id_cc=id_cc)
    provinciaEditar.nombre_cc = nombre_cc
    provinciaEditar.codigo_cc = codigo_cc
    provinciaEditar.foto_cc = foto_cc
    provinciaEditar.save()

    messages.success(request, 'Provincia actualizada exitosamente')
    return redirect('/listadoProvincias')





#TIPOS
def listadoTipos(request):
    tipoBdd=Tipo.objects.all()
    return render(request,'listadoTipos.html',{'tipos':tipoBdd})

def guardarTipo(request):
    nombre_cc=request.POST["nombre_cc"]
    dificultad_cc=request.POST["dificultad_cc"]
    descripcion_cc=request.POST["descripcion_cc"]

    nuevoTipo = Tipo.objects.create(
        nombre_cc=nombre_cc,
        dificultad_cc=dificultad_cc,
        descripcion_cc=descripcion_cc,
    )

    messages.success(request, 'Tipo guardado exitosamente')
    return redirect('/listadoTipos')


def eliminarTipo(request,id_cc):
    eliminarTipo=Tipo.objects.get(id_cc=id_cc)
    eliminarTipo.delete()
    return redirect('/listadoTipos')

def editarTipo(request, id_cc):
    tipoEditar = Tipo.objects.get(id_cc=id_cc)
    return render(request, 'editarTipo.html', {'tipo': tipoEditar})


def procesarActualizacionTipo(request, id_cc):
    id_cc = request.POST["id_cc"]
    nombre_cc = request.POST["nombre_cc"]
    dificultad_cc = request.POST["dificultad_cc"]
    descripcion_cc = request.POST["descripcion_cc"]

    tipoEditar = Tipo.objects.get(id_cc=id_cc)
    tipoEditar.nombre_cc = nombre_cc
    tipoEditar.dificultad_cc = dificultad_cc
    tipoEditar.descripcion_cc = descripcion_cc
    tipoEditar.save()

    messages.success(request, 'Tipo actualizado Exitosamente')
    return redirect('/listadoTipos')




#INGREDIENTES
def listadoIngredientes(request):
    ingredienteBdd=Ingrediente.objects.all()
    return render(request,'listadoIngredientes.html',{'ingredientes':ingredienteBdd})

def guardarIngrediente(request):
    nombre_cc=request.POST["nombre_cc"]
    tipo_cc=request.POST["tipo_cc"]
    foto_cc=request.FILES.get("foto_cc")

    nuevoIngrediente = Ingrediente.objects.create(
        nombre_cc=nombre_cc,
        tipo_cc=tipo_cc,
        foto_cc=foto_cc,
    )

    messages.success(request, 'Ingrediente guardado exitosamente')
    return redirect('/listadoIngredientes')


def eliminarIngrediente(request,id_cc):
    eliminarIngrediente=Ingrediente.objects.get(id_cc=id_cc)
    eliminarIngrediente.delete()
    return redirect('/listadoIngredientes')

def editarIngrediente(request, id_cc):
    ingredienteEditar = Ingrediente.objects.get(id_cc=id_cc)
    return render(request, 'editarIngrediente.html', {'ingrediente': ingredienteEditar})


def procesarActualizacionIngrediente(request, id_cc):
    id_cc = request.POST["id_cc"]
    nombre_cc = request.POST["nombre_cc"]
    tipo_cc = request.POST["tipo_cc"]
    foto_cc=request.FILES.get("foto_cc")

    ingredienteEditar = Ingrediente.objects.get(id_cc=id_cc)
    ingredienteEditar.nombre_cc = nombre_cc
    ingredienteEditar.tipo_cc = tipo_cc
    ingredienteEditar.foto_cc = foto_cc
    ingredienteEditar.save()

    messages.success(request, 'Ingrediente actualizado Exitosamente')
    return redirect('/listadoIngredientes')


#CLIENTE


def listadoClientes(request):
    clientesBdd=Cliente.objects.all()
    provinciaBdd=Provincia.objects.all()
    return render(request,'listadoClientes.html',{'clientes':clientesBdd,'provincias':provinciaBdd})

def guardarCliente(request):
    id_provincia=request.POST["id_provincia"]
    provinciaSeleccionado=Provincia.objects.get(id_cc=id_provincia)
    cedula_cc=request.POST["cedula_cc"]
    nombre_cc=request.POST["nombre_cc"]
    correo_cc=request.POST["correo_cc"]

    nuevoCliente = Cliente.objects.create(
        provincia_cc=provinciaSeleccionado,
        cedula_cc=cedula_cc,
        nombre_cc=nombre_cc,
        correo_cc=correo_cc,
    )

    messages.success(request, 'Cliente guardado exitosamente')
    return redirect('/listadoClientes')


def eliminarCliente(request,id_cc):
    eliminarCliente=Cliente.objects.get(id_cc=id_cc)
    eliminarCliente.delete()
    return redirect('/listadoClientes')

def editarCliente(request, id_cc):
    clienteEditar = Cliente.objects.get(id_cc=id_cc)
    provinciaBdd=Provincia.objects.all()
    return render(request, 'editarCliente.html', {'cliente': clienteEditar,'provincia':provinciaBdd})


def procesarActualizacionCliente(request, id_cc):
    id_cc= request.POST["id_cc"]
    id_provincia = request.POST["id_provincia"]
    provinciaSeleccionado=Provincia.objects.get(id_ac=id_provincia)
    cedula_cc = request.POST["cedula_cc"]
    nombre_cc = request.POST["nombre_cc"]
    correo_cc = request.POST["correo_cc"]

    clienteEditar = Cliente.objects.get(id_cc=id_cc)
    clienteEditar.provincia_cc = provinciaSeleccionado
    clienteEditar.cedula_cc = cedula_cc
    clienteEditar.nombre_cc = nombre_cc
    clienteEditar.correo_cc = correo_cc
    clienteEditar.save()

    messages.success(request, 'Cliente actualizado Exitosamente')
    return redirect('/listadoClientes')



#PEDIDOS

def listadoPedidos(request):
    pedidosBdd=Pedido.objects.all()
    clientesBdd=Cliente.objects.all()
    return render(request,'listadoPedidos.html',{'pedidos':pedidosBdd,'clientes':clientesBdd})

def guardarPedido(request):
    id_cliente=request.POST["id_cliente"]
    clienteSeleccionado=Cliente.objects.get(id_cc=id_cliente)
    fecha_cc=request.POST["fecha_cc"]
    tipopago_cc=request.POST["tipopago_cc"]
    servicio_cc=request.POST["servicio_cc"]

    nuevoPedido = Pedido.objects.create(
        cliente_cc=clienteSeleccionado,
        fecha_cc=fecha_cc,
        tipopago_cc=tipopago_cc,
        servicio_cc=servicio_cc,
    )

    messages.success(request, 'Pedido guardado exitosamente')
    return redirect('/listadoPedidos')


def eliminarPedido(request,id_cc):
    eliminarPedido=Pedido.objects.get(id_cc=id_cc)
    eliminarPedido.delete()
    return redirect('/listadoPedidos')

def editarPedido(request, id_cc):
    pedidoEditar = Pedido.objects.get(id_cc=id_cc)
    clientesBdd=Cliente.objects.all()
    return render(request, 'editarPedido.html', {'cliente': clientesBdd,'pedido':pedidoEditar})


def procesarActualizacionPedido(request, id_cc):
    id_cc= request.POST["id_cc"]
    id_cliente = request.POST["id_cliente"]
    clienteSeleccionado=Cliente.objects.get(id_cc=id_cliente)
    fecha_cc = request.POST["fecha_cc"]
    tipopago_cc = request.POST["tipopago_cc"]
    servicio_cc = request.POST["servicio_cc"]

    pedidoEditar = Pedido.objects.get(id_cc=id_cc)
    pedidoEditar.cliente_cc = clienteSeleccionado
    pedidoEditar.fecha_cc = fecha_cc
    pedidoEditar.tipopago_cc = tipopago_cc
    pedidoEditar.servicio_cc = servicio_cc
    pedidoEditar.save()

    messages.success(request, 'Cliente actualizado Exitosamente')
    return redirect('/listadoPedidos')




#PLATILLOS

def listadoPlatillos(request):
    platilloBdd=Platillo.objects.all()
    tipoBdd=Tipo.objects.all()
    return render(request,'listadoPlatillos.html',{'platillos':platilloBdd,'tipos':tipoBdd})

def guardarPlatillo(request):
    id_tipo=request.POST["id_tipo"]
    tipoSeleccionado=Tipo.objects.get(id_cc=id_tipo)
    nombre_cc=request.POST["nombre_cc"]
    costou_cc=request.POST["costou_cc"]
    foto_cc=request.FILES.get("foto_cc")

    nuevoPlatillos = Platillo.objects.create(
        tipo_cc=tipoSeleccionado,
        nombre_cc=nombre_cc,
        costou_cc=costou_cc,
        foto_cc=foto_cc,
    )

    messages.success(request, 'Platillo guardado exitosamente')
    return redirect('/listadoPlatillos')


def eliminarPlatillo(request,id_cc):
    eliminarPlatillo=Platillo.objects.get(id_cc=id_cc)
    eliminarPlatillo.delete()
    return redirect('/listadoPlatillos')

def editarPlatillo(request, id_cc):
    platillosEditar = Platillo.objects.get(id_cc=id_cc)
    tipoBdd=Tipo.objects.all()
    return render(request, 'editarPlatillo.html', {'platillo': platillosEditar,'tipo':tipoBdd})


def procesarActualizacionPlatillo(request, id_cc):
    id_cc= request.POST["id_cc"]
    id_tipo = request.POST["id_tipo"]
    tipoSeleccionado=Tipo.objects.get(id_cc=id_tipo)
    nombre_cc = request.POST["nombre_cc"]
    costou_cc = request.POST["costou_cc"]
    foto_cc=request.FILES.get("foto_cc")

    platilloEditar = Platillo.objects.get(id_cc=id_cc)
    platilloEditar.tipo_cc = tipoSeleccionado
    platilloEditar.nombre_cc = nombre_cc
    platilloEditar.costou_cc = costou_cc
    platilloEditar.foto_cc = foto_cc
    platilloEditar.save()

    messages.success(request, 'Pĺatillo actualizado Exitosamente')
    return redirect('/listadoPlatillos')


#DETALLES

def listadoDetalles(request):
    detalleBdd=Detalle.objects.all()
    pedidoBdd=Pedido.objects.all()
    platilloBdd=Platillo.objects.all()
    return render(request,'listadoDetalles.html',{'detalles':detalleBdd, 'platillos':platilloBdd,'pedidos':pedidoBdd})

def guardarDetalle(request):

    id_pedido=request.POST["id_pedido"]
    pedidoSeleccionado=Pedido.objects.get(id_cc=id_pedido)
    mesa_cc=request.POST["mesa_cc"]
    descripcion_cc=request.POST["descripcion_cc"]
    costot_cc=request.POST["costot_cc"]
    id_platillo_seleccionados = request.POST.getlist("id_platillo")

    nuevoDetalle = Detalle.objects.create(
        pedido_cc=pedidoSeleccionado,
        mesa_cc=mesa_cc,
        descripcion_cc=descripcion_cc,
        costot_cc=costot_cc,
    )
    nuevoDetalle.platillo_cc.add(*id_platillo_seleccionados)

    messages.success(request, 'Detalle guardado exitosamente')
    return redirect('/')




def eliminarDetalle(request,id_cc):
    eliminarDetalle=Detalle.objects.get(id_cc=id_cc)
    eliminarDetalle.delete()
    return redirect('/')

def editarDetalle(request, id_cc):
    detalleEditar = Detalle.objects.get(id_cc=id_cc)
    platilloBdd=Platillo.objects.all()
    pedidoBdd=Pedido.objects.all()
    return render(request, 'editarDetalle.html', {'detalle':detalleEditar,'platillo': platilloBdd,'pedido':pedidoBdd})


def procesarActualizacionDetalle(request, id_cc):
    id_cc= request.POST["id_cc"]
    id_pedido = request.POST["id_pedido"]
    pedidoSeleccionado=Pedido.objects.get(id_cc=id_pedido)
    mesa_cc = request.POST["mesa_cc"]
    descripcion_cc = request.POST["descripcion_cc"]
    costot_cc = request.POST["costot_cc"]

    nuevos_platillos = request.POST.getlist("id_platillo")

    detalleEditar = Detalle.objects.get(id_cc=id_cc)

    detalleEditar.platillo_cc.clear()
    detalleEditar.platillo_cc.add(*nuevos_platillos)

    detalleEditar = Detalle.objects.get(id_cc=id_cc)
    detalleEditar.pedido_cc = pedidoSeleccionado
    detalleEditar.mesa_cc = mesa_cc
    detalleEditar.descripcion_cc = descripcion_cc
    detalleEditar.costot_cc = costot_cc
    detalleEditar.save()

    messages.success(request, 'Detalle actualizado Exitosamente')
    return redirect('/')



#RECETAS

def listadoRecetas(request):
    recetaBdd=Receta.objects.all()
    ingredienteBdd=Ingrediente.objects.all()
    platilloBdd=Platillo.objects.all()
    return render(request,'listadoRecetas.html',{'recetas':recetaBdd, 'platillos':platilloBdd,'ingredientes':ingredienteBdd})

def guardarReceta(request):
    id_platillo=request.POST["id_platillo"]
    platilloSeleccionado=Platillo.objects.get(id_cc=id_platillo)
    tiempo_cc=request.POST["tiempo_cc"]
    origen_cc=request.POST["origen_cc"]
    indicaciones_cc=request.POST["indicaciones_cc"]
    id_ingredientes_seleccionados = request.POST.getlist("id_ingrediente")

    nuevoReceta = Receta.objects.create(
        platillo_cc=platilloSeleccionado,
        tiempo_cc=tiempo_cc,
        origen_cc=origen_cc,
        indicaciones_cc=indicaciones_cc,
    )
    nuevoReceta.ingrediente_cc.add(*id_ingredientes_seleccionados)

    messages.success(request, 'Receta guardada exitosamente')
    return redirect('/listadoRecetas')


def eliminarReceta(request,id_cc):
    eliminarReceta=Receta.objects.get(id_cc=id_cc)
    eliminarReceta.delete()
    return redirect('/listadoRecetas')

def editarReceta(request, id_cc):
    recetaEditar = Receta.objects.get(id_cc=id_cc)
    platilloBdd=Platillo.objects.all()
    ingredienteBdd=Ingrediente.objects.all()
    return render(request, 'editarReceta.html', {'receta':recetaEditar,'platillos': platilloBdd,'ingredientes':ingredienteBdd})


def procesarActualizacionReceta(request, id_cc):
    id_cc= request.POST["id_cc"]
    id_platillo = request.POST["id_platillo"]
    platilloSeleccionado=Platillo.objects.get(id_cc=id_platillo)
    tiempo_cc = request.POST["tiempo_cc"]
    origen_cc = request.POST["origen_cc"]
    indicaciones_cc = request.POST["indicaciones_cc"]
    nuevos_ingredientes = request.POST.getlist("id_ingrediente")

    recetaEditar = Receta.objects.get(id_cc=id_cc)

    recetaEditar.ingrediente_cc.clear()
    recetaEditar.ingrediente_cc.add(*nuevos_ingredientes)

    recetaEditar = Receta.objects.get(id_cc=id_cc)
    recetaEditar.platillo_cc = platilloSeleccionado
    recetaEditar.tiempo_cc  = tiempo_cc
    recetaEditar.origen_cc = origen_cc
    recetaEditar.indicaciones_cc = indicaciones_cc
    recetaEditar.save()

    messages.success(request, 'Receta actualizada Exitosamente')
    return redirect('/listadoRecetas')






#GENERACION REPORTEA
def reportes(request):
    detalleBdd=Detalle.objects.all()
    pedidoBdd=Pedido.objects.all()

    return render(request, 'reportes.html',{'detalles':detalleBdd, 'pedidos':pedidoBdd})
