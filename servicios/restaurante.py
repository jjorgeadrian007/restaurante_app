class Restaurante:
    def __init__(self, nombre_restaurante):
        self.nombre_restaurante = nombre_restaurante
        self.menu_productos = [] 
        self.clientes_registrados = [] 

    def registrar_producto(self, producto):
        self.menu_productos.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes_registrados.append(cliente)

    def mostrar_resumen_dia(self):
        print(f"\n=== RESTAURANTE: {self.nombre_restaurante} ===")
        print("\n MENÚ DISPONIBLE:")

        for prod in self.menu_productos:
            print(f"  • {prod}") 

        print("\n CLIENTES ATENDIDOS Y SU CUENTA:")
        for cli in self.clientes_registrados:
            print(f"\n{cli}:")
            
            total = 0
            for prod in cli.consumo:
                print(f"  - {prod.nombre}: ${prod.precio:.2f}")
                total += prod.precio
            print(f"Total a pagar: ${total:.2f}")