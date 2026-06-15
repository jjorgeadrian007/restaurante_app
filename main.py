from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


mi_restaurante = Restaurante("La Sazón Universitaria")

# 2. Crear  productos 
plato1 = Producto("Almuerzo Ejecutivo", 3.50)
plato2 = Producto("Porción de Papas", 1.50)
bebida1 = Producto("Jugo Natural", 1.00)

# Registrar los productos en el menú del restaurante
mi_restaurante.registrar_producto(plato1)
mi_restaurante.registrar_producto(plato2)
mi_restaurante.registrar_producto(bebida1)

# 3. Crear clientes (objetos de la clase Cliente)
cliente1 = Cliente("Adrian")
cliente2 = Cliente("Maria")

# Registrar clientes en el restaurante
mi_restaurante.registrar_cliente(cliente1)
mi_restaurante.registrar_cliente(cliente2)

print("--- PEDIDOS ---")
# 4. Realizar su pedidos
cliente1.ordenar_producto(plato1)
cliente1.ordenar_producto(bebida1)

cliente2.ordenar_producto(plato2)
cliente2.ordenar_producto(bebida1)

# 5. Mostrar todo lo registrado de forma organizada en la consola
mi_restaurante.mostrar_resumen_dia()