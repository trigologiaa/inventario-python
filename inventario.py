import sqlite3


class Inventario:
    """
    Clase encargada de gestionar la base de datos 'inventario.db'.
    Contiene métodos CRUD para el manejo de productos.
    """

    def __init__(self, base_de_datos: str = "inventario.db") -> None:
        """
        Inicializa la clase con la base de datos y la creación de la tabla de
        productos.
        """
        self.base_de_datos = base_de_datos
        self.conexion = sqlite3.connect(self.base_de_datos)
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self) -> None:
        """
        Crea la tabla 'productos' si no existe.
        """
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT
            );
            """
        )
        self.conexion.commit()

    def registrar_producto(
        self,
        nombre: str,
        descripcion: str,
        cantidad: int,
        precio: float,
        categoria: str,
    ) -> None:
        """
        Registra un nuevo producto en la tabla.
        """
        self.cursor.execute(
            """
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
            """,
            (nombre, descripcion, cantidad, precio, categoria),
        )
        self.conexion.commit()

    def obtener_productos(self) -> list:
        """
        Retorna todos los productos almacenados.
        """
        self.cursor.execute("SELECT * FROM productos;")
        return self.cursor.fetchall()

    def buscar_por_id(self, id: int) -> tuple | None:
        """
        Busca un producto por su ID.
        Retorna una tupla con el producto o None si no existe.
        """
        try:
            id = int(id)
        except (TypeError, ValueError):
            return None
        self.cursor.execute(
            """
            SELECT *
            FROM productos
            WHERE id = ?
            """,
            (id,),
        )
        return self.cursor.fetchone()

    def actualizar_producto(
        self,
        id: int,
        nombre: str,
        descripcion: str,
        cantidad: int,
        precio: float,
        categoria: str,
    ) -> None:
        """
        Actualiza un producto identificado por su ID.
        """
        self.cursor.execute(
            """
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
            """,
            (nombre, descripcion, cantidad, precio, categoria, id),
        )
        self.conexion.commit()

    def eliminar_producto(self, id: int) -> tuple | bool:
        """
        Elimina un producto por ID. Retorna True si se eliminó, False si no existía.
        """
        try:
            id = int(id)
        except (ValueError, TypeError):
            return False
        self.cursor.execute(
            """
            SELECT *
            FROM productos
            WHERE id = ?
            """,
            (id,),
        )
        producto = self.cursor.fetchone()
        if not producto:
            return False
        self.cursor.execute(
            """
            DELETE FROM productos WHERE id = ?
            """,
            (id,),
        )
        self.conexion.commit()
        return producto

    def productos_bajo_stock(self, limite: int) -> list:
        """
        Devuelve productos con cantidad <= límite.
        """
        try:
            limite = int(limite)
        except (ValueError, TypeError):
            return []
        self.cursor.execute(
            """
            SELECT *
            FROM productos
            WHERE cantidad <= ?
            """,
            (limite,),
        )
        return self.cursor.fetchall()

    def cerrar(self) -> None:
        """
        Cierra la conexión con la base de datos.
        """
        self.conexion.close()
