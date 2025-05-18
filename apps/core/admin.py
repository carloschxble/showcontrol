from django.contrib import admin
from .models import *

# Registro del modelo Emprendedor en el admin
@admin.register(Emprendedor)
class EmprendedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_emprendimiento', 'renta_mensual', 'activo', 'correo', 'telefono') # Campos que se mostrarán en la lista de emprendedores
    search_fields = ('nombre', 'nombre_emprendimiento', 'correo') # Campos que se podrán buscar en el buscador del admin
    list_filter = ('activo',) # Filtros para facilitar la búsqueda por estado activo/inactivo

# Registro del modelo PeriodoActividad en el admin
@admin.register(PeriodoActividad)
class PeriodoActividadAdmin(admin.ModelAdmin):
    list_display = ('emprendedor', 'fecha_alta', 'fecha_baja', 'esta_activo') # Campos visibles en la lista de periodos de actividad
    list_filter = ('fecha_alta', 'fecha_baja') # Filtros para buscar por fechas de alta y baja
    search_fields = ('emprendedor__nombre',) # Buscar por nombre del emprendedor relacionado

    def esta_activo(self, obj):
        return obj.esta_activo()
    
    esta_activo.boolean = True
    esta_activo.short_description = 'Activo'

# Registro del modelo Venta en el admin
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('emprendedor', 'codigo_producto', 'nombre_producto', 'precio_unitario', 'cantidad', 'total', 'fecha_venta') # Columnas que aparecerán en la lista de ventas
    list_filter = ('fecha_venta',) # Filtro por fecha de venta para agilizar la búsqueda
    search_fields = ('codigo_producto', 'nombre_producto', 'emprendedor__nombre') # Búsqueda por código y nombre de producto, así como por emprendedor
    readonly_fields = ('total',)  # Esto evita que se edite y lo muestra como solo lectura en el formulario

# Registro del modelo RentaPago en el admin
@admin.register(RentaPago)
class RentaPagoAdmin(admin.ModelAdmin):
    list_display = ('emprendedor', 'fecha_pago', 'monto', 'pagado') # Campos visibles en la lista de pagos de renta
    list_filter = ('pagado', 'fecha_pago') # Filtros para separar pagos realizados y pendientes, y filtrar por fecha
    search_fields = ('emprendedor__nombre',) # Buscar por nombre del emprendedor