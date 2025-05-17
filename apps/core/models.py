from django.db import models
from django.utils import timezone

from django.db import models
from django.utils import timezone

# Modelo principal para representar a cada emprendedor que renta un espacio
class Emprendedor(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre de la persona emprendedora
    nombre_emprendimiento = models.CharField(max_length=150)  # Nombre de su marca o negocio
    renta_mensual = models.DecimalField(max_digits=8, decimal_places=2)  # Cuánto paga mensualmente
    activo = models.BooleanField(default=True)  # Si actualmente tiene o no el espacio activo
    correo = models.EmailField(blank=True, null=True)  # Correo (opcional)
    telefono = models.CharField(max_length=10, blank=True, null=True)  # Teléfono (opcional)

    def __str__(self):
        return f'{self.nombre} - {self.nombre_emprendimiento}'


# Modelo para llevar un historial de los periodos de alta y baja de cada emprendedor
class PeriodoActividad(models.Model):
    emprendedor = models.ForeignKey(
        Emprendedor, 
        on_delete=models.CASCADE, 
        related_name='periodos'
    )
    fecha_alta = models.DateField(default=timezone.now)  # Cuándo comenzó a rentar
    fecha_baja = models.DateField(null=True, blank=True)  # Cuándo dejó de rentar (puede ser None si sigue activo)

    def esta_activo(self):
        # Devuelve True si aún no tiene fecha de baja o si la fecha de baja es en el futuro
        return self.fecha_baja is None or self.fecha_baja > timezone.now().date()

    def __str__(self):
        return f'{self.emprendedor.nombre} activo desde {self.fecha_alta} hasta {self.fecha_baja or "actualidad"}'
    

# Modelo que representa cada venta que realiza un emprendedor
class Venta(models.Model):
    emprendedor = models.ForeignKey(
        Emprendedor, 
        on_delete=models.CASCADE, 
        related_name='ventas'
    )
    codigo_producto = models.CharField(max_length=50)  # Código del producto (puede venir de Eleventa)
    nombre_producto = models.CharField(max_length=100)  # Nombre del producto
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)  # Precio por unidad
    cantidad = models.PositiveIntegerField()  # Cuántas unidades vendió
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # Total calculado automáticamente
    fecha_venta = models.DateField()  # Cuándo se hizo la venta

    def save(self, *args, **kwargs):
        # Calcula el total antes de guardar: precio por cantidad
        self.total = self.precio_unitario * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre_producto} vendido por {self.emprendedor.nombre_emprendimiento} el {self.fecha_venta}'
    

# Modelo para registrar los pagos mensuales de renta de cada emprendedor
class RentaPago(models.Model):
    emprendedor = models.ForeignKey(
        Emprendedor, 
        on_delete=models.CASCADE, 
        related_name='rentas'
    )
    fecha_pago = models.DateField()  # Fecha en que se hizo o se debería hacer el pago
    monto = models.DecimalField(max_digits=10, decimal_places=2)  # Monto de la renta (puede coincidir con renta_mensual)
    pagado = models.BooleanField(default=False)  # Si ya fue pagado o aún está pendiente

    def __str__(self):
        return f'Renta {self.monto} para {self.emprendedor.nombre} pagado: {self.pagado} en {self.fecha_pago}'