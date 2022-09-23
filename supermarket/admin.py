from django.contrib import admin

# Register your models here.

from .models import Categoria
from .models import Producto
from .models import Detalle
from .models import Venta
from .models import Direccion
from .models import Cliente
from .models import Telefono
from .models import Proveedor

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Detalle)
admin.site.register(Venta)
admin.site.register(Direccion)
admin.site.register(Cliente)
admin.site.register(Telefono)
admin.site.register(Proveedor)