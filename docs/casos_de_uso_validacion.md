# Casos de Uso de Validación de Entrada

Este documento describe detalladamente los casos de prueba y de uso para verificar que las validaciones de entrada en la interfaz gráfica del Árbol Binario de Búsqueda (ABB) funcionen correctamente de acuerdo a los requerimientos del tutor y sin romper el comportamiento de la aplicación.

---

## 1. Casos de Éxito (Tipos de Enteros Soportados)

Estos valores deben ser aceptados por el campo de entrada, procesados correctamente como enteros en la lógica del árbol y representados en el canvas y los recorridos.

| Caso de Uso | Entrada de Ejemplo | Valor Esperado (Decimal) | Comportamiento en la Interfaz |
| :--- | :--- | :--- | :--- |
| **Entero Positivo Estándar** | `42` | `42` | Se agrega el nodo `42` al árbol correctamente. |
| **Entero con Signo Positivo Explicito** | `+15` | `15` | Se agrega el nodo `15` al árbol correctamente. |
| **Entero Negativo** | `-8` | `-8` | Se agrega el nodo `-8` al árbol correctamente (se posiciona a la izquierda si la raíz es mayor). |
| **Entero Hexadecimal** | `0x1A` | `26` | Se agrega el nodo `26` al árbol. |
| **Entero Binario** | `0b1101` | `13` | Se agrega el nodo `13` al árbol. |
| **Entero Octal** | `0o17` | `15` | Se agrega el nodo `15` al árbol. |
| **Espacios Adicionales** | `  -5  ` | `-5` | Se eliminan los espacios extremos y se agrega el nodo `-5`. |

---

## 2. Casos de Error (Entradas Inválidas)

Estas entradas deben ser rechazadas de inmediato por la validación de la interfaz, mostrando un cuadro de diálogo de error de Tkinter y sin alterar el estado del árbol.

### A. Campo Vacío / Solo Espacios
- **Entrada:** ` ` o dejar en blanco.
- **Mensaje de Error esperado:** *"El campo no puede estar vacío"* (Título: *Error*).
- **Resultado:** No se altera el árbol ni se limpia el campo de texto.

### B. Valores No Numéricos o Caracteres Especiales
- **Entrada:** `abc`, `12a`, `++5`, `--10`, `@`, `0x`, `0b`, `12-3`.
- **Mensaje de Error esperado:** *"Solo se permiten números enteros"* (Título: *Error*).
- **Resultado:** No se altera el árbol.

### C. Números Decimales (Flotantes)
- **Entrada:** `12.5`, `3.0`, `-1.5`.
- **Mensaje de Error esperado:** *"Solo se permiten números enteros"* (Título: *Error*).
- **Resultado:** No se altera el árbol (ya que representan números de coma flotante, no enteros).

### D. Valores fuera de Rango (Desbordamiento de 32 bits)
- **Entrada (Límite Superior):** `2147483648` (o superior).
- **Entrada (Límite Inferior):** `-2147483649` (o inferior).
- **Mensaje de Error esperado:** *"El valor excede el rango de un entero de 32 bits (-2147483648 a 2147483647)"* (Título: *Error*).
- **Resultado:** Previene desbordamiento en memoria y visualización. El árbol no se modifica.

---

## 3. Validaciones Propias del Árbol (Reglas de Negocio)

Estas validaciones ocurren a nivel de la estructura del árbol posterior a la validación de tipos enteros y también deben comportarse correctamente.

1. **No Duplicados (RN3):**
   - Si se ingresa un valor entero válido que ya existe en el árbol (ej. agregar `5` dos veces).
   - **Resultado esperado:** Muestra ventana de error *"No se permiten duplicados"*.
2. **Límite de Altura / Niveles (RF19/RN8):**
   - Si se intenta insertar un nodo que generaría un nivel mayor a 4 (ej. en una secuencia de orden `1, 2, 3, 4, 5`).
   - **Resultado esperado:** Muestra ventana de error *"No se puede exceder los 4 niveles"*.
