# Sistema de Inventario - Python + SQLite

Un sistema de inventario simple y completo desarrollado en Python, utilizando
SQLite como base de datos y con una interfaz de consola mejorada con **Colorama**.
Permite realizar todas las operaciones CRUD: **crear, leer, actualizar y eliminar
productos**, además de generar reportes y cargar productos de prueba
automáticamente.

---

## Características principales

- CRUD completo de productos.
- Base de datos local SQLite (`inventario.db`).
- Validaciones de datos robustas.
- Prevención de errores comunes del usuario.
- Reporte de productos con bajo stock.
- Eliminación con confirmación.
- Carga opcional de _100 productos aleatorios_.
- Código organizado usando clases (`Inventario`, `Menu`).
- Interfaz más clara usando Colorama.

---

## Tecnologías utilizadas

- **Python 3.13.0+**
- **SQLite3**
- **Colorama** (para colores en terminal)
- **Random / Faker (opcional)** para datos aleatorios
- Programación orientada a objetos (POO)

---

## Estructura del proyecto

```txt
inventario-python
├── __init__.py
├── inventario.py
├── main.py
├── menu.py
├── README.md
├── requirements.txt
└── utils.py
```

### Descripción de archivos

| Archivo         | Descripción                                     |
| --------------- | ----------------------------------------------- |
| \_\_init\_\_.py | Archivo que contiene el módulo.                 |
| main.py         | Punto de entrada del programa. Ejecuta el menú. |
| menu.py         | Interacción con el usuario.                     |
| inventario.py   | Manejo de las operaciones con la base de datos. |
| utils.py        | Funciones auxiliares.                           |

---

## Requisitos

- Python 3.13+.
- `pip` instalado.

---

## Instalación

1. **Clonar el repositorio**

   ```sh
   # SSH
   git clone git@github.com:trigologiaa/inventario-python.git

   # HTTPS
   git clone https://github.com/trigologiaa/inventario-python.git

   # Moverse al directorio
   cd inventario-python
   ```

2. **Crear un entorno virtual (opcional pero recomendado)**

   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instalar dependencias**

   ```sh
   # Requiere entorno virtual
   pip install -r requirements.txt
   ```

---

## Ejecutar el sistema

Desde la terminal:

```sh
python main.py
```

---

## Funcionalidades del sistema

### Registrar producto

Permite ingresar un producto con validación de:

- Nombre no vacío
- Categoría no vacía
- Cantidad ≥ 0
- Precio ≥ 0

---

### Ver productos

Muestra todos los productos almacenados en la base de datos.

---

### Actualizar producto (por ID)

Permite modificar cualquier campo.

Los campos pueden quedar en blanco para mantener su valor actual.

---

### Eliminar producto (por ID)

Realiza:

- Validación del ID
- Verificación de existencia
- Eliminación y muestra del producto eliminado

---

### Buscar producto (por ID)

Muestra un único producto.

También valida el ID ingresado.

---

### Reporte de bajo stock

Permite ingresar un número límite y muestra los productos con:

```txt
cantidad <= límite
```

---

### Cargar 100 productos aleatorios (opcional al iniciar)

Al iniciar el sistema, el usuario puede elegir:

```txt
¿Deseás cargar 100 productos aleatorios? (s/n)
```

Sirve para pruebas rápidas sin necesidad de cargar datos manualmente.

---

## Datos aleatorios

Los productos generados al azar incluyen:

- Nombres ficticios
- Categorías comunes
- Cantidades entre 1 y 100
- Precios entre 100 y 10.000
- Descripciones simples

---

## Base de datos

La tabla `productos` contiene:

| Campo       | Tipo                              |
| ----------- | --------------------------------- |
| id          | INTEGER PRIMARY KEY AUTOINCREMENT |
| nombre      | TEXT NOT NULL                     |
| descripcion | TEXT                              |
| cantidad    | INTEGER NOT NULL                  |
| precio      | REAL NOT NULL                     |
| categoria   | TEXT                              |

---

## Ejemplo de uso

```txt
==============================
     SISTEMA DE INVENTARIO
==============================

1. Registrar producto
2. Ver productos
3. Actualizar producto por ID
4. Eliminar producto por ID
5. Buscar producto por ID
6. Reporte bajo stock
7. Salir

Seleccioná una opción:
```

---

## Licencia

Este proyecto utiliza una licencia MIT.
