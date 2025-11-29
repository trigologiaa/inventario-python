import os
import random
from colorama import Fore, Style, init

init(autoreset=True)


def limpiar_pantalla() -> None:
    """
    Limpia la pantalla según el sistema operativo.
    """
    os.system("cls" if os.name == "nt" else "clear")


def pausar() -> None:
    """
    Pausa la ejecución para que el usuario pueda leer el contenido.
    """
    input(Fore.MAGENTA + "\nPresioná Enter para continuar..." + Style.RESET_ALL)


def cargar_productos_aleatorios(inventario, cantidad=100):
    """
    Carga una cantidad determinada de productos aleatorios en la base de datos.
    """
    nombres = [
        "Laptop",
        "Mouse",
        "Teclado",
        "Monitor",
        "Silla",
        "Escritorio",
        "Auriculares",
        "Micrófono",
        "Cámara",
        "Impresora",
        "Router",
        "USB",
        "Parlante",
        "Tablet",
        "Smartphone",
        "Lámpara",
        "Mochila",
        "Cable HDMI",
        "Disco SSD",
        "Fuente de poder",
    ]
    categorias = ["Electrónica", "Computación", "Oficina", "Accesorios", "Audio"]
    for _ in range(cantidad):
        nombre = random.choice(nombres)
        descripcion = f"{nombre} de excelente calidad"
        cantidad_prod = random.randint(1, 500)
        precio = round(random.uniform(10.0, 5000.0), 2)
        categoria = random.choice(categorias)
        inventario.registrar_producto(
            nombre, descripcion, cantidad_prod, precio, categoria
        )
    print(
        Fore.GREEN
        + f"\nSe cargaron {cantidad} productos aleatorios correctamente."
        + Style.RESET_ALL
    )
