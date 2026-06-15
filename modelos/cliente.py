
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.consumo = []  

    def ordenar_producto(self, producto):
        """Agrega un producto a la lista de consumo del cliente"""
        self.consumo.append(producto)
        print(f"Productos {self.nombre} ordenó: {producto}")

    def __str__(self):
        return f"Cliente: {self.nombre}"
    


