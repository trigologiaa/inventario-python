from colorama import Fore, Style
from inventario import Inventario
from utils import limpiar_pantalla, pausar, cargar_productos_aleatorios


class Menu:
    """
    Clase encargada de mostrar el menú principal e interactuar con el usuario.
    Llama a los métodos de la base de datos según la opción elegida.
    """

    def __init__(self) -> None:
        """
        Inicializa la clase del menú instanciando el inventario.
        """
        self.db = Inventario()
        limpiar_pantalla()
        print(Fore.CYAN + "¿Deseás cargar 100 productos aleatorios?" + Style.RESET_ALL)
        opcion = input(Fore.YELLOW + "(s/n): " + Style.RESET_ALL).strip().lower()
        if opcion == "s":
            print("Cargando productos. Aguardá un momento...")
            cargar_productos_aleatorios(self.db)
            pausar()

    def mostrar_menu(self) -> None:
        """
        Muestra el menú de opciones.
        """
        while True:
            limpiar_pantalla()
            print(Fore.CYAN + "==============================")
            print("     SISTEMA DE INVENTARIO    ")
            print("==============================" + Style.RESET_ALL)
            print(Fore.YELLOW + "1." + Style.RESET_ALL, "Registrar producto")
            print(Fore.YELLOW + "2." + Style.RESET_ALL, "Ver productos")
            print(Fore.YELLOW + "3." + Style.RESET_ALL, "Actualizar producto por ID")
            print(Fore.YELLOW + "4." + Style.RESET_ALL, "Eliminar producto por ID")
            print(Fore.YELLOW + "5." + Style.RESET_ALL, "Buscar producto por ID")
            print(Fore.YELLOW + "6." + Style.RESET_ALL, "Reporte bajo stock")
            print(Fore.YELLOW + "7." + Style.RESET_ALL, "Salir")
            opcion = input(Fore.GREEN + "\nSeleccioná una opción: " + Style.RESET_ALL)
            if opcion == "1":
                self.registrar_producto()
            elif opcion == "2":
                self.ver_productos()
            elif opcion == "3":
                self.actualizar_producto()
            elif opcion == "4":
                self.eliminar_producto()
            elif opcion == "5":
                self.buscar_producto()
            elif opcion == "6":
                self.reporte_bajo_stock()
            elif opcion == "7":
                print(Fore.CYAN + "Saliendo del sistema..." + Style.RESET_ALL)
                self.db.cerrar()
                break
            else:
                print(Fore.RED + "Opción inválida." + Style.RESET_ALL)
                pausar()

    def registrar_producto(self) -> None:
        """
        Registra el producto en la base de datos.
        """
        limpiar_pantalla()
        print(Fore.CYAN + "Registrar producto" + Style.RESET_ALL)
        while True:
            nombre = input("Nombre: ").strip()
            if nombre:
                break
            print(Fore.RED + "El nombre no puede estar vacío." + Style.RESET_ALL)
        descripcion = input("Descripción: ").strip()
        while True:
            categoria = input("Categoría: ").strip()
            if categoria:
                break
            print(Fore.RED + "La categoría no puede estar vacía." + Style.RESET_ALL)
        while True:
            try:
                cantidad = int(input("Cantidad: "))
                if cantidad < 0:
                    raise ValueError
                break
            except ValueError:
                print(
                    Fore.RED
                    + "La cantidad debe ser un número entero válido y no negativo."
                    + Style.RESET_ALL
                )
        while True:
            try:
                precio = float(input("Precio: "))
                if precio < 0:
                    raise ValueError
                break
            except ValueError:
                print(
                    Fore.RED
                    + "El precio debe ser un número válido (puede ser entero o decimal) y no negativo."
                    + Style.RESET_ALL
                )
        self.db.registrar_producto(nombre, descripcion, cantidad, precio, categoria)
        print(Fore.GREEN + "Producto registrado exitosamente." + Style.RESET_ALL)
        pausar()

    def ver_productos(self) -> None:
        """
        Muestra los productos en la pantalla.
        """
        limpiar_pantalla()
        print(Fore.CYAN + "Lista de productos" + Style.RESET_ALL)
        productos = self.db.obtener_productos()
        for p in productos:
            print(p)
        pausar()

    def actualizar_producto(self) -> None:
        """
        Actualiza la información del producto con validación completa.
        """
        limpiar_pantalla()
        print(Fore.CYAN + "Actualizar producto" + Style.RESET_ALL)
        while True:
            try:
                producto_id = int(input("ID del producto: "))
                break
            except ValueError:
                print(
                    Fore.RED
                    + "El ID debe ser un número entero válido."
                    + Style.RESET_ALL
                )
        producto = self.db.buscar_por_id(producto_id)
        if not producto:
            print(Fore.RED + "No existe un producto con ese ID." + Style.RESET_ALL)
            pausar()
            return
        print(
            Fore.YELLOW
            + "\nDejá el campo vacío para mantener el valor actual.\n"
            + Style.RESET_ALL
        )
        actual_nombre = producto[1]
        actual_descripcion = producto[2]
        actual_cantidad = producto[3]
        actual_precio = producto[4]
        actual_categoria = producto[5]
        nombre = input(f"Nombre ({actual_nombre}): ").strip() or actual_nombre
        descripcion = (
            input(f"Descripción ({actual_descripcion}): ").strip() or actual_descripcion
        )
        categoria = (
            input(f"Categoría ({actual_categoria}): ").strip() or actual_categoria
        )
        while True:
            cantidad_input = input(f"Cantidad ({actual_cantidad}): ").strip()
            if cantidad_input == "":
                cantidad = actual_cantidad
                break
            try:
                cantidad = int(cantidad_input)
                if cantidad < 0:
                    raise ValueError
                break
            except ValueError:
                print(
                    Fore.RED
                    + "La cantidad debe ser un número entero válido y no negativo."
                    + Style.RESET_ALL
                )
        while True:
            precio_input = input(f"Precio ({actual_precio}): ").strip()
            if precio_input == "":
                precio = actual_precio
                break
            try:
                precio = float(precio_input)
                if precio < 0:
                    raise ValueError
                break
            except ValueError:
                print(
                    Fore.RED
                    + "El precio debe ser un número válido y no negativo."
                    + Style.RESET_ALL
                )
        self.db.actualizar_producto(
            producto_id, nombre, descripcion, cantidad, precio, categoria
        )
        print(Fore.GREEN + "\nProducto actualizado correctamente." + Style.RESET_ALL)
        pausar()

    def eliminar_producto(self) -> None:
        """
        Elimina el producto de la base de datos.
        """
        limpiar_pantalla()
        print(Fore.CYAN + "Eliminar producto" + Style.RESET_ALL)
        try:
            producto_id = int(input("ID del producto: "))
        except ValueError:
            print(
                Fore.RED + "ID inválido. Debe ser un número entero." + Style.RESET_ALL
            )
            pausar()
            return
        producto_eliminado = self.db.eliminar_producto(producto_id)
        if not producto_eliminado:
            print(Fore.RED + "No existe un producto con ese ID." + Style.RESET_ALL)
            pausar()
            return
        print(Fore.GREEN + "Producto eliminado correctamente." + Style.RESET_ALL)
        print(Fore.YELLOW + f"Eliminado: {producto_eliminado}" + Style.RESET_ALL)
        pausar()

    def buscar_producto(self) -> None:
        """
        Busca el producto por el ID.
        """
        limpiar_pantalla()
        print(Fore.CYAN + "Buscar producto por ID" + Style.RESET_ALL)
        try:
            producto_id = int(input("ID del producto: "))
        except ValueError:
            print(
                Fore.RED + "ID inválido. Debe ser un número entero." + Style.RESET_ALL
            )
            pausar()
            return
        producto = self.db.buscar_por_id(producto_id)
        if producto:
            print(Fore.YELLOW + "\nProducto encontrado:" + Style.RESET_ALL)
            print(producto)
        else:
            print(Fore.RED + "No existe un producto con ese ID." + Style.RESET_ALL)
        pausar()

    def reporte_bajo_stock(self) -> None:
        """
        Muestra los productos con stock menor o igual a un número dado.
        """
        limpiar_pantalla()
        print(Fore.CYAN + "Reporte de bajo stock" + Style.RESET_ALL)
        try:
            limite = int(input("Mostrar productos con cantidad <= : "))
            if limite <= 0:
                print(
                    Fore.RED
                    + "El límite debe ser un número entero mayor a 0."
                    + Style.RESET_ALL
                )
                pausar()
                return
        except ValueError:
            print(
                Fore.RED
                + "Valor inválido. Debe ingresar un número entero."
                + Style.RESET_ALL
            )
            pausar()
            return
        productos = self.db.productos_bajo_stock(limite)
        print(Fore.YELLOW + "\nProductos con bajo stock:" + Style.RESET_ALL)
        if not productos:
            print(
                Fore.CYAN
                + "No hay productos con stock menor o igual a ese límite."
                + Style.RESET_ALL
            )
        else:
            for p in productos:
                print(p)
        pausar()
